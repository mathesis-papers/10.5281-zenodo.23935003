import itertools
import json
from fractions import Fraction


def parameters(ratio, scale, level):
    return (ratio * ratio + 1) / (ratio + 1), scale * ratio ** level


def neighbors(vertex, branching):
    level, branch, word = vertex
    if branch is None:
        return [(level - 1, None, ()), (level + 1, None, ())] + [
            (level, index, ()) for index in range(branching - 1)
        ]
    parent = (level, branch, word[:-1]) if word else (level, None, ())
    return [parent] + [(level, branch, word + (index,)) for index in range(branching)]


def length(first, second, ratio, scale):
    if first[1] is None and second[1] is None:
        coefficient, size = parameters(ratio, scale, min(first[0], second[0]))
        return coefficient * size
    return scale * ratio ** (first[0] if first[1] is not None else second[0])


def vertex_ratio(vertex, branching, ratio, scale):
    lengths = [length(vertex, other, ratio, scale) for other in neighbors(vertex, branching)]
    reciprocal_sum = sum((1 / edge for edge in lengths), Fraction(0))
    square_sum = sum((1 / edge ** 2 for edge in lengths), Fraction(0))
    return reciprocal_sum / square_sum


def check_parameter_identities():
    count = 0
    for branching, ratio, scale, level in itertools.product(
        (2, 3, 4, 5, 9, 31),
        (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3)),
        (Fraction(1), Fraction(7, 5)),
        range(-8, 9),
    ):
        coefficient, size = parameters(ratio, scale, level)
        incident = [coefficient * size / ratio, coefficient * size] + [size] * (branching - 1)
        reciprocal_sum = sum((1 / edge for edge in incident), Fraction(0))
        square_sum = sum((1 / edge ** 2 for edge in incident), Fraction(0))
        assert all(edge > 0 for edge in incident)
        assert reciprocal_sum / square_sum == size
        assert (size ** 2 + (ratio * size) ** 2) / (coefficient * size) - size - ratio * size == 0
        assert 2 * size ** 2 / size - 2 * size == 0
        assert (coefficient == 1) == (ratio == 1)
        count += 1
    return count


def check_neighborhoods():
    vertices_checked = 0
    oriented_edges_checked = 0
    for branching, ratio in itertools.product((2, 3, 4, 5), (Fraction(1, 2), Fraction(2))):
        for level in range(-3, 4):
            vertices = [(level, None, ())]
            for branch in range(branching - 1):
                for depth in range(4):
                    vertices.extend((level, branch, word) for word in itertools.product(range(branching), repeat=depth))
            for vertex in vertices:
                adjacent = neighbors(vertex, branching)
                assert len(set(adjacent)) == branching + 1
                assert vertex not in adjacent
                first_ratio = vertex_ratio(vertex, branching, ratio, Fraction(1))
                assert first_ratio == ratio ** level
                if vertex[1] is not None:
                    assert len({length(vertex, other, ratio, Fraction(1)) for other in adjacent}) == 1
                for other in adjacent:
                    assert vertex in neighbors(other, branching)
                    edge = length(vertex, other, ratio, Fraction(1))
                    assert edge > 0 and edge == length(other, vertex, ratio, Fraction(1))
                    second_ratio = vertex_ratio(other, branching, ratio, Fraction(1))
                    assert (first_ratio ** 2 + second_ratio ** 2) / edge - first_ratio - second_ratio == 0
                    oriented_edges_checked += 1
                vertices_checked += 1
    return vertices_checked, oriented_edges_checked


def inverse_line_length(pattern, level):
    value = Fraction(1)
    if level > 0:
        for index in range(1, level + 1):
            value *= pattern[index % len(pattern)]
    elif level < 0:
        for index in range(level + 1, 1):
            value /= pattern[index % len(pattern)]
    return value


def line_ratio(pattern, level):
    previous = inverse_line_length(pattern, level - 1)
    following = inverse_line_length(pattern, level)
    return (previous + following) / (previous ** 2 + following ** 2)


def extended_length(first, second, pattern):
    if first[1] is None and second[1] is None:
        return 1 / inverse_line_length(pattern, min(first[0], second[0]))
    level = first[0] if first[1] is not None else second[0]
    return line_ratio(pattern, level)


def extended_ratio(vertex, branching, pattern):
    lengths = [extended_length(vertex, other, pattern) for other in neighbors(vertex, branching)]
    return sum((1 / edge for edge in lengths), Fraction(0)) / sum(
        (1 / edge ** 2 for edge in lengths), Fraction(0)
    )


def check_extensions():
    cases_checked = 0
    vertices_checked = 0
    edges_checked = 0
    for period in range(1, 5):
        for pattern in itertools.product((2, 3), repeat=period):
            for branching in (2, 3, 5):
                cases_checked += 1
                for level in range(-3, 4):
                    assert inverse_line_length(pattern, level) / inverse_line_length(pattern, level - 1) == pattern[level % period]
                    vertices = [(level, None, ())]
                    for branch in range(branching - 1):
                        vertices.extend([(level, branch, ()), (level, branch, (0,))])
                    for vertex in vertices:
                        adjacent = neighbors(vertex, branching)
                        assert len(set(adjacent)) == branching + 1
                        first_ratio = extended_ratio(vertex, branching, pattern)
                        assert first_ratio == line_ratio(pattern, level)
                        if vertex[1] is not None:
                            assert len({extended_length(vertex, other, pattern) for other in adjacent}) == 1
                        for other in adjacent:
                            assert vertex in neighbors(other, branching)
                            edge = extended_length(vertex, other, pattern)
                            assert edge > 0 and edge == extended_length(other, vertex, pattern)
                            second_ratio = extended_ratio(other, branching, pattern)
                            assert (first_ratio ** 2 + second_ratio ** 2) / edge - first_ratio - second_ratio == 0
                            edges_checked += 1
                        vertices_checked += 1
    return cases_checked, vertices_checked, edges_checked


def check_ratio_preservation():
    cases_checked = 0
    for degree in (1, 2, 3):
        for lengths in itertools.product((Fraction(1, 2), Fraction(1), Fraction(3, 2)), repeat=degree):
            reciprocal_sum = sum((1 / edge for edge in lengths), Fraction(0))
            square_sum = sum((1 / edge ** 2 for edge in lengths), Fraction(0))
            original_ratio = reciprocal_sum / square_sum
            for additions in range(1, 6):
                assert (reciprocal_sum + additions / original_ratio) / (
                    square_sum + additions / original_ratio ** 2
                ) == original_ratio
                cases_checked += 1
    return cases_checked


def curvature(first, second, branching, ratio):
    first_edges = [length(first, other, ratio, Fraction(1)) for other in neighbors(first, branching)]
    second_edges = [length(second, other, ratio, Fraction(1)) for other in neighbors(second, branching)]
    first_squares = sum((1 / edge ** 2 for edge in first_edges), Fraction(0))
    second_squares = sum((1 / edge ** 2 for edge in second_edges), Fraction(0))
    edge = length(first, second, ratio, Fraction(1))
    first_ratio = vertex_ratio(first, branching, ratio, Fraction(1))
    second_ratio = vertex_ratio(second, branching, ratio, Fraction(1))
    return 2 * (1 / first_squares + 1 / second_squares) / edge ** 2 - (first_ratio + second_ratio) / edge


def check_curvatures():
    cases_checked = 0
    for branching, ratio, level in itertools.product(
        (2, 3, 4, 5, 9, 31),
        (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 2), Fraction(2), Fraction(3)),
        range(-3, 4),
    ):
        factor = branching - 1 + (ratio + 1) ** 2 / (ratio ** 2 + 1)
        spine = (level, None, ())
        branch_root = (level, 0, ())
        branch_child = (level, 0, (0,))
        inside = curvature(branch_root, branch_child, branching, ratio)
        attachment = curvature(spine, branch_root, branching, ratio)
        assert inside == Fraction(4, branching + 1) - 2
        assert attachment == 2 / factor + Fraction(2, branching + 1) - 2
        assert attachment > inside
        cases_checked += 1
    return cases_checked


def main():
    identities = check_parameter_identities()
    vertices, edges = check_neighborhoods()
    patterns, extension_vertices, extension_edges = check_extensions()
    ratio_cases = check_ratio_preservation()
    curvature_cases = check_curvatures()
    result = {
        "arithmetic": "exact rational arithmetic using Python fractions.Fraction",
        "parameter_cases": identities,
        "neighborhood_vertices": vertices,
        "oriented_edge_residuals": edges,
        "parameter_scope": {
            "q": [2, 3, 4, 5, 9, 31],
            "r": ["1/3", "1/2", "2/3", "1", "3/2", "2", "3"],
            "t": ["1", "7/5"],
            "n": [-8, 8],
        },
        "neighborhood_scope": {"q": [2, 3, 4, 5], "r": ["1/2", "2"], "n": [-3, 3], "branch_word_lengths": [0, 3]},
        "extension_cases": patterns,
        "extension_vertices": extension_vertices,
        "extension_oriented_edge_residuals": extension_edges,
        "extension_scope": {
            "q": [2, 3, 5],
            "periodic_reciprocal_ratio_patterns": "All words over {2, 3} of lengths 1 through 4, repeated periodically",
            "n": [-3, 3],
            "vertices_per_level": "Spine, every branch root, and each root's child indexed 0; complete neighbor sets at each sampled vertex",
        },
        "ratio_preservation_cases": ratio_cases,
        "ratio_preservation_scope": "All incident length lists of sizes 1 through 3 over {1/2, 1, 3/2}, with 1 through 5 equal-ratio attachments",
        "curvature_cases": curvature_cases,
        "curvature_scope": {"q": [2, 3, 4, 5, 9, 31], "r": ["1/3", "1/2", "2/3", "3/2", "2", "3"], "n": [-3, 3]},
        "cubic_curvatures": {"branch": "-2/3", "attachment": "-13/21"},
        "coverage": "Finite exact checks of positivity, degrees, symmetry, equal branch stars, vertex ratios, zero edge residuals, ratio-preserving extensions, and curvature formulas. Infinite statements and acyclicity have written proofs in note.tex; the two-choice line classification is Theorem 10 of arXiv:2006.06716v1.",
        "cubic_distinct_lengths": ["1", "5/3"],
        "all_assertions_satisfied": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
