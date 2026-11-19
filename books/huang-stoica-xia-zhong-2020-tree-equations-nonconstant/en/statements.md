# Exact statements and complete proofs

We construct the regular tree, verify every edge equation, and prove the extension by constant-length branches. The remaining conclusions follow from this construction and the source's line-solution classification.

## Equations and domain

Let $H$ be a connected, locally finite simple tree with at least one edge and symmetric positive edge lengths $\ell_{ij}=\ell_{ji}>0$. Every vertex has a neighbor, so the following finite sums and ratios are strictly positive:

$$
\begin{aligned}
c_i&=\sum_{j\sim i}\ell_{ij}^{-1},\\
d_i&=\sum_{j\sim i}\ell_{ij}^{-2},\\
R_i&=c_i/d_i>0.
\end{aligned}
$$

For adjacent vertices of a tree, the unique simple path is their edge. Removing backtracking from any other finite walk reduces its length. Thus their shortest-path length equals $\ell_{ij}$, and equation (3.1) of Huang and colleagues becomes

$$
\mathcal E_{ij}=\frac{R_i^2+R_j^2}{\ell_{ij}}-R_i-R_j=0.
$$

No boundary condition at infinity is imposed. Write $T_q$ for the infinite $(q+1)$-regular tree.

## The geometric-spine family

::: {.theorem #geometric-family title="Geometric-spine family" status="written-proof" proof="pf-geometric-family" doi="10.5281/zenodo.23935004" source="Theorem 1, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/125" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s1"}
Fix an integer $q\ge2$, a scale $t>0$ and a real $r>0$ with $r\ne1$. Set

$$
s_n=tr^n\quad(n\in\mathbb Z),
\qquad a=\frac{r^2+1}{r+1}.
$$

On a bi-infinite spine $(v_n)$, give edge $v_nv_{n+1}$ length $as_n$. Attach $q-1$ disjoint rooted $q$-ary trees at each $v_n$; every edge in these branches, including each attachment, has length $s_n$. This is a positive nonconstant solution on $T_q$. The ratio is $R_i=s_n$ at $v_n$ and at every vertex in a branch attached there.
:::

::: {.proof #pf-geometric-family}
Index the vertices of each branch by finite words over $\{1,\ldots,q\}$. Join the empty word to $v_n$, and join each word to its $q$ one-letter extensions. Use disjoint copies for different branches and different $n$. Each spine vertex has two spine neighbors and $q-1$ branch neighbors; each branch vertex has one parent and $q$ children. The graph is simple, locally finite and has degree $q+1$ everywhere. Following parents reaches the spine in finitely many steps, proving connectedness. The spine and each branch are acyclic, and each branch has exactly one attachment, so no cycle can leave a branch through the spine and return. This realizes $T_q$.

All lengths are positive and symmetric. The incident lengths at $v_n$ are $as_n/r$, $as_n$ and $q-1$ copies of $s_n$, giving

$$
c_{v_n}=s_n^{-1}\left(\frac{r+1}{a}+q-1\right),
$$

$$
d_{v_n}=s_n^{-2}\left(\frac{r^2+1}{a^2}+q-1\right).
$$

Since $a(r+1)=r^2+1$, the two parenthesized factors are equal and positive. Hence $R_{v_n}=s_n$. Every branch vertex has $q+1$ incident edges of length $s_n$, so $c_i=(q+1)/s_n$, $d_i=(q+1)/s_n^2$ and again $R_i=s_n$.

A branch or attachment edge has both endpoint ratios and length equal to $s_n$, giving residual $2s_n^2/s_n-2s_n=0$. A spine edge has endpoint ratios $s_n$ and $rs_n$, giving

$$
\mathcal E_{v_nv_{n+1}}
=s_n\left(\frac{1+r^2}{a}-1-r\right)=0.
$$

These cases exhaust all edges; the residual is symmetric in the endpoints. Finally, the attachment at $v_0$ has length $t$ and the next spine edge has length $at$, while

$$
a-1=\frac{r(r-1)}{r+1}\ne0.
$$

Thus the solution is nonconstant.
:::
::: {.corollary #conjecture-refutations title="Counterexamples to the source conjectures" status="written-proof" proof="pf-conjecture-refutations" doi="10.5281/zenodo.23935004" source="Corollary 2, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/126" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s2"}
Conjecture 4 of Huang and colleagues, §5.2, printed page 32, is false. For every $q\ge2$, their Conjecture 3 on the same page is false on $T_q$, even if equal incident lengths are required at every vertex outside a bi-infinite path.
:::

::: {.proof #pf-conjecture-refutations}
Take $q=r=2$, $t=1$ in [@geometric-family]. This is a positive nonconstant solution on $T_2$, refuting Conjecture 4. For any $q\ge2$, take, for example, $r=2,t=1$. There is at least one branch at each spine vertex, every vertex off the spine has equal incident lengths, and the solution is globally nonconstant. This refutes Conjecture 3.
:::

### The exact conclusion of the public Lean theorem

The next statement isolates the public declaration's logical form. It is distinct from the all-parameter corollary above.

::: {.theorem #cubic-negation title="Negation of cubic-tree constancy" lean="D5/S3/Geometry/DiscreteGravity/TreeEquationsNonconstantRefutation.result" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s2"}
The universal assertion that every positive symmetric edge-length solution of the local equations on a locally finite cubic tree is constant on all edges is false.
:::

::: {.proof #pf-cubic-negation}
The public proof constructs the $q=r=2,t=1$ tree on $\mathbb Z\sqcup(\mathbb Z\times\mathrm{List}(\mathrm{Bool}))$. Integers index the spine, and finite Boolean words index its binary branches. It checks local finiteness, degree three, connectedness and acyclicity, positivity and symmetry. It computes both vertex ratios as $2^n$ and checks all edge residuals. Finally, an attachment of length $1$ and a neighboring spine edge of length $5/3$ contradict any common constant. The public theorem states the negation of the universal proposition; the concrete construction occurs internally in its proof.
:::

## Extension by filling missing branches

::: {.lemma #branch-extension title="Extension preserving the original ratios" status="written-proof" proof="pf-branch-extension" doi="10.5281/zenodo.23935004" source="Lemma 3, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/127" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s3"}
Let $q\ge2$ be an integer and $H$ a connected locally finite tree with at least one edge and degrees at most $q+1$. Every positive solution on $H$ extends to a positive solution on $T_q$, preserving every original edge length and vertex ratio. At $i\in H$, attach $m_i=q+1-\deg_H(i)$ disjoint rooted $q$-ary trees and give every edge in each new branch, including its attachment, length $R_i$.
:::

::: {.proof #pf-branch-extension}
Connectedness and the existence of an edge imply that every original vertex has positive degree, so $c_i,d_i,R_i>0$. Each $m_i$ is a nonnegative integer; when $m_i=0$, no branch is added there. Build disjoint branches by the finite-word construction above. The new graph is connected and acyclic. Each original vertex now has degree $q+1$, and each new vertex has one parent and $q$ children. Thus the enlarged graph is $T_q$.

At an original vertex the new sums satisfy

$$
c'_i=c_i+\frac{m_i}{R_i},
\qquad d'_i=d_i+\frac{m_i}{R_i^2}.
$$

Using $c_i=R_i d_i$, we obtain

$$
R_i d'_i=R_i d_i+\frac{m_i}{R_i}=c'_i.
$$

Since $d'_i>0$, it follows that $R'_i=R_i$. Every new vertex in a branch attached at $i$ has all incident lengths $R_i$ and therefore ratio $R_i$. The original edges retain both their lengths and endpoint ratios, so their equations remain valid. Every new edge, including each attachment, has residual $2R_i^2/R_i-2R_i=0$.
:::
::: {.corollary #two-choice-patterns title="Arbitrary two-choice spine patterns" status="written-proof" proof="pf-two-choice-patterns" doi="10.5281/zenodo.23935004" source="Corollary 4, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/128" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s4"}
Fix an integer $q\ge2$, any bi-infinite sequence $b_n\in\{2,3\}$ and $L_0>0$. Define positive spine-edge lengths by $L_{n-1}/L_n=b_n$, where $L_n$ is the length of $v_nv_{n+1}$. There is a solution on $T_q$ with these spine lengths. Every vertex outside the spine has equal incident lengths, while the solution is nonconstant. If both choices occur, the spine lengths are not a single geometric progression.
:::

::: {.proof #pf-two-choice-patterns}
Recursing by division in the positive direction and multiplication in the negative direction gives a unique positive value at each integer index. This is the parameter-$2$ instance of Huang and colleagues' Theorem 10, §5.1, printed pages 28–29: the other allowed ratio is $(2+1)/(2-1)=3$. For a self-contained dependency chain here, we also verify this instance directly.

At line vertex $v_n$, the incident lengths are $b_nL_n$ and $L_n$, so

$$
R_n=L_n\frac{b_n(b_n+1)}{b_n^2+1}=\frac65L_n,
$$

where the last equality holds for both $b_n=2$ and $b_n=3$. On edge $v_nv_{n+1}$ put $b=b_{n+1}$, so $L_{n+1}=L_n/b$. Hence

$$
\begin{aligned}
\mathcal E_{n,n+1}
&=L_n\Big[\frac{36}{25}(1+b^{-2})\\
&\qquad-\frac65(1+b^{-1})\Big]\\
&=0
\end{aligned}.
$$

Indeed, multiplying the bracket by $25b^2$ gives

$$
\begin{aligned}
&36(b^2+1)-30(b^2+b)\\
&\qquad=6(b-2)(b-3)=0.
\end{aligned}
$$

Thus every two-choice sequence, including a nonperiodic one, gives a line solution. Since every ratio is at least $2$, $L_n$ is strictly decreasing and nonconstant. Apply [@branch-extension], adding $q-1$ branches at each line vertex. The original lengths and nonconstancy are preserved, and all off-spine vertices have equal incident lengths. If both ratios occur, the successive length ratio is not constant, excluding a single geometric progression.
:::
::: {.corollary #constant-ratios title="Constant lengths exactly when ratios are constant" status="written-proof" proof="pf-constant-ratios" doi="10.5281/zenodo.23935004" source="Corollary 5, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/129" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s5"}
For a positive solution on a connected locally finite tree with at least one edge, the edge lengths are globally constant if and only if the vertex ratios $R_i$ are globally constant.
:::

::: {.proof #pf-constant-ratios}
If every $R_i=s$, positivity and the absence of isolated vertices give $s>0$. The equation on each edge becomes $2s^2/\ell_{ij}-2s=0$; divide by $2s$ to obtain $\ell_{ij}=s$. Conversely, if every edge has length $s>0$, each vertex has positive finite degree and

$$
c_i=\frac{\deg(i)}s,
\qquad d_i=\frac{\deg(i)}{s^2}.
$$

Therefore $R_i=s$ everywhere, proving both directions.
:::

## Curvature and boundary behavior

Use Huang and colleagues' equation (4.10), printed page 13:

$$
K_{ij}=\frac2{\ell_{ij}^2}\left(\frac1{d_i}+\frac1{d_j}\right)
-\frac{R_i+R_j}{\ell_{ij}}.
$$

::: {.corollary #nonconstant-curvature title="Nonconstant curvature of the geometric spine" status="written-proof" proof="pf-nonconstant-curvature" doi="10.5281/zenodo.23935004" source="Corollary 6, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/130" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s6"}
Every nonconstant solution in [@geometric-family] has nonconstant tree curvature. Put $B=q-1+(r+1)^2/(r^2+1)$. The curvatures of an interior branch edge and an attachment edge are respectively

$$
K_{\mathrm{branch}}=\frac4{q+1}-2,
$$

$$
K_{\mathrm{attach}}=\frac2B+\frac2{q+1}-2,
$$

with $K_{\mathrm{attach}}>K_{\mathrm{branch}}$. For $q=r=2$ the values are $-2/3$ and $-13/21$.
:::

::: {.proof #pf-nonconstant-curvature}
At a spine vertex $d_i=B/s_n^2$; at a branch vertex $d_i=(q+1)/s_n^2$. Both endpoints of an interior branch edge have the latter type; an attachment joins one endpoint of each type. Both edge types have length $s_n$ and both endpoint ratios $s_n$. Substitution into the curvature formula gives the two displayed expressions.

Since $(r-1)^2>0$, we have $(r+1)^2<2(r^2+1)$, so $0<B<q+1$. Therefore

$$
K_{\mathrm{attach}}-K_{\mathrm{branch}}
=\frac2B-\frac2{q+1}>0.
$$

Both edge types exist because $q\ge2$. At $q=r=2$, $B=1+9/5=14/5$, giving $K_{\mathrm{branch}}=4/3-2=-2/3$ and $K_{\mathrm{attach}}=5/7+2/3-2=-13/21$.
:::

At $r=1$ the same formulas give $a=1$ and $s_n=t$, recovering the constant solution and zero curvature difference. This is the equality case excluded by nonconstancy. If $r>1$, $s_n$ tends to zero as $n\to-\infty$ and to infinity as $n\to+\infty$; for $0<r<1$ the directions reverse. These are limits of geometric sequences, with no infinite sum or interchange of limits. The family therefore fails the asymptotically constant boundary condition in Huang and colleagues' Definition 13 and Theorem 2.

At a spine vertex the three lengths $as_n/r$, $as_n$ and $s_n$ are pairwise distinct when $r\ne1$. We already proved $a\ne1$. Equality $a/r=1$ would give $r^2+1=r(r+1)$, hence $r=1$; equality of the first two also forces $r=1$. Thus these examples do not satisfy the half-half grouping hypotheses of the source's Theorems 11–12. Its Remark 12 already gives non-half-half examples for odd $q$; this family also covers every even $q\ge2$. A general classification of scale patterns does not follow from these results.
