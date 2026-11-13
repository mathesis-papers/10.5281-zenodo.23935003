# Positive nonconstant solutions of the tree equations

This package gives counterexamples to Conjectures 3 and 4 in Section 5.2,
printed page 32, of Huang, Stoica, Xia and Zhong, arXiv:2006.06716v1.
For each integer q ≥ 2, real r > 0 with r ≠ 1 and t > 0, a bi-infinite
spine with constant-length attached branches solves the edge equations.
The complete proof, the cubic example and a source-item coverage table
are in `note.tex` and `note.pdf`.
An extension principle preserves any positive solution on a nontrivial tree
of maximum degree at most q+1 by adding constant-length branches to obtain
T_q. It lifts all the source's positive line solutions to higher degree,
including arbitrary {2,3} reciprocal-ratio sequences. The note also proves
a global constant-ratio criterion and explicit nonconstant-curvature formulas.

## Contents and rebuilding

- `note.tex`: self-contained main source, including bibliography.
- `metadata.json`: authors, license, problem identifier and scientific scope.
- `coverage.json`: source-item mapping and Lean, written-proof and finite-check scopes.
- `verify.py`: standard-library Python 3 exact-rational checks.
- `verification.json`: expected checker output.

Build with **Tectonic 0.17.0**:

```sh
tectonic note.tex
```

Alternatively run `pdflatex -interaction=nonstopmode -halt-on-error note.tex`
twice. The bibliography is embedded, so BibTeX is unnecessary.

Reproduce the finite checks:

```sh
python3 verify.py > computed.json
python3 -c 'import json; assert json.load(open("computed.json")) == json.load(open("verification.json"))'
```

The checks cover the parameter and neighborhood ranges recorded in
`verification.json`; they do not replace the written proof for arbitrary
real parameters and the infinite graph.

## Mathematical coverage

`result : ¬ claim` in the namespace
`D5.S3.Geometry.DiscreteGravity.TreeEquationsNonconstantRefutation` proves
the failure of global constancy for positive symmetric solutions on a
locally finite cubic tree, using the instance q = r = 2 and t = 1.
The pinned source is:

https://github.com/the-omega-institute/trureturing/blob/50f2a97bb5e704842f2c32c6095f68a0dc62c779/D5/S3/Geometry/DiscreteGravity/TreeEquationsNonconstantRefutation.lean

The general q, r, t family, the equal-star counterexample to Conjecture 3,
the extension principle, the global constant-ratio criterion and the
curvature formulas have written proofs in the note. The two-choice line
construction uses Theorem 10 of the posing paper (printed pp. 28–29).
The q = 1 case of Conjecture 3 is already
Theorem 9 of the posing paper. Boundary-value uniqueness, half-half
classification and the action conjectures are not contradicted by this family.

## Authors and license

Haobo Ma — ChronoAI Pte Ltd, Singapore.

Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

Copyright 2026 Haobo Ma and Wenlin Zhang. Licensed under Creative Commons
Attribution 4.0 International (CC BY 4.0):
https://creativecommons.org/licenses/by/4.0/ .
