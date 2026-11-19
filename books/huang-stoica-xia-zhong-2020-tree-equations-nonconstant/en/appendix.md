# Evidence and references

## What the Lean statement checks

The [pinned Lean proof](lean:D5/S3/Geometry/DiscreteGravity/TreeEquationsNonconstantRefutation.result) establishes the cubic counterexample. The table below separates that result from the broader written theorems.

The declaration below proves the negation of the universal cubic-tree constancy proposition in [@cubic-negation]. Its proof constructs a fixed infinite witness, not a finite sampled neighborhood. Positivity and symmetry are required on edges, the graph is locally finite and a tree, every degree is three, and every edge residual vanishes. There is no boundary condition or uniform positive lower bound. Decidable adjacency is included in the Lean proposition.


The definitions of reciprocal sums, their ratio and the residual agree with the technical chapter on this domain. Lean's totalized real division causes no extra case here: positivity and a nonempty finite neighbor set give $c_i,d_i>0$. Values assigned to nonedges have no mathematical role in the claim. The graph and explicit lengths, ratio computations and residual checks are private construction lemmas inside the public proof; the public conclusion is `¬ claim`.

| Manuscript statement | Exact correspondence |
| --- | --- |
| Theorem 1: all $q,t,r$ and explicit ratios | The public proof supplies the fixed $q=r=2,t=1$ case internally; it does not state the parameterized family. |
| Corollary 2: both conjectures, all $q\ge2$ | The public theorem gives the cubic constancy negation. The equal-star counterexamples in all degrees need a broader declaration. |
| Lemma 3: arbitrary input tree extension | Written proof; no matching public statement in the inspected DiscreteGravity module. |
| Corollary 4: every bi-infinite two-choice sequence | Written proof using the earlier line classification, with a direct algebraic check in this explanation. |
| Corollary 5: the global iff criterion | Written proof of both directions; distinct from one nonconstant witness. |
| Corollary 6: two curvature formulas and strict inequality | Written proof; the public cubic negation contains no curvature conclusion. |

The infinite statements rely on their complete proofs. Finite rational checks illustrate selected inputs.

## Contribute a precise missing statement

The existing written proofs are mathematical results. Their shared requests identify the remaining formalization work:

- [Theorem 1, Section 1: Geometric-spine solutions on every regular tree](https://github.com/the-omega-institute/trureturing-requests/issues/125).
- [Corollary 2, Section 1: Equal-star rigidity fails on every regular tree](https://github.com/the-omega-institute/trureturing-requests/issues/126).
- [Lemma 3, Section 2: Extend a tree solution by constant-length branches](https://github.com/the-omega-institute/trureturing-requests/issues/127).
- [Corollary 4, Section 2: Arbitrary two-choice spine patterns on regular trees](https://github.com/the-omega-institute/trureturing-requests/issues/128).
- [Corollary 5, Section 2: Constant lengths if and only if constant vertex ratios](https://github.com/the-omega-institute/trureturing-requests/issues/129).
- [Corollary 6, Section 3: Nonconstant curvature of geometric-spine solutions](https://github.com/the-omega-institute/trureturing-requests/issues/130).

Choose a shared issue to coordinate the mathematical scope, and follow the [contribution guide](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md) to submit a proof. Preserve credit for the original results and earlier literature.

## Paper identity and citation

Cite version 2 with DOI **10.5281/zenodo.23935004**. The concept DOI **10.5281/zenodo.23935003** identifies the version collection. The paper is available under CC BY 4.0.

## References

1. Haobo Ma and Wenlin Zhang. *Counterexamples to Conjectures 3 and 4 of Huang, Stoica, Xia and Zhong (arXiv:2006.06716v1, Section 5.2, printed page 32)*, version 2 (2026). [Exact-version DOI](https://doi.org/10.5281/zenodo.23935004). [Version collection](https://doi.org/10.5281/zenodo.23935003). CC BY 4.0.
2. A. Huang, B. Stoica, X. Xia and X. Zhong. *Bounds on the Ricci curvature and solutions to the Einstein equations for weighted graphs* (2020). [arXiv:2006.06716v1](https://arxiv.org/abs/2006.06716v1). Equation (3.1): tree equations; Theorem 10, §5.1, printed pp. 28–29: line classification; Conjectures 3–4, §5.2, printed p. 32: questions refuted here; equation (4.10), printed p. 13: curvature. Definition 13 and Theorem 2 impose the separate asymptotically constant boundary condition.
3. S. S. Gubser, M. Heydeman, C. Jepsen, M. Marcolli, S. Parikh, I. Saberi, B. Stoica and B. Trundy. *Edge length dynamics on graphs with applications to $p$-adic AdS/CFT*. J. High Energy Phys. **2017**, 157 (2017). [DOI](https://doi.org/10.1007/JHEP06(2017)157); [arXiv:1612.09580v1](https://arxiv.org/abs/1612.09580v1), §5, equations (97)–(99): prior odd-$q$ constructions.
4. S. Bai, H. Cheng and B. Hua. *Discrete Einstein metrics on trees*, [arXiv:2604.22449v3](https://arxiv.org/abs/2604.22449v3) (2026), §1. Cited in the source for constant-curvature metrics on finite trees, a different problem.
5. H. Cheng. *Positive-Curvature Discrete Einstein Metrics on Trees*, [arXiv:2605.20862v2](https://arxiv.org/abs/2605.20862v2) (2026), §1. The same distinction between constant curvature and the present tree equations applies.
