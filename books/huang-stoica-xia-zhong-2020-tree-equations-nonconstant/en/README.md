# Can one tidy junction determine a whole network?

Give every edge of an infinitely branching tree a positive length. Suppose every edge obeys the same local balance equation, and many junctions have equal lengths all around them. Must every edge in the whole tree have the same length? Haobo Ma and Wenlin Zhang construct a counterexample: lengths change along one path running infinitely in both directions, while every junction away from that path is completely uniform. The construction works in every constant degree at least three. It disproves two conjectures in a 2020 paper by Huang, Stoica, Xia and Zhong.

This is an explanation of version 2 of Ma and Zhang's paper. We begin with fractions and a small part of the network; [the technical chapter](statements.md) then gives all parameters and complete proofs. Haobo Ma is affiliated with Chrono AI, Singapore. Wenlin Zhang is affiliated with the National University of Singapore and Chrono AI, Singapore.

## Start with an ordinary tree-shaped network

Think of vertices as junctions and edges as road segments. A tree is connected and has no cycles: between any two vertices there is exactly one path that does not revisit a vertex. An edge's length is a number assigned to it, rather than the distance measured in a drawing. Assigning a positive number to every edge gives a tree with lengths.

The degree of a vertex counts its incident edges. The notation $T_q$ means an infinite tree with $q+1$ edges at every vertex. Thus $T_2$ has three edges at every junction and is called a cubic, or 3-regular, tree. It is different from a line, which has degree two. An infinite tree can still have finitely many neighbors at each vertex; this is local finiteness.

Equal lengths give an obvious candidate solution. The question is whether the equations allow anything else. The equations studied by Huang and colleagues come from graph versions of curvature and Einstein equations. To understand this counterexample, we need the explicit rule that relates neighboring lengths.

## How a junction reads its neighboring lengths

At vertex $i$, add the reciprocals of the incident lengths to obtain $c_i$. Add the squares of those reciprocals to obtain $d_i$. Define the junction's effective length as $R_i=c_i/d_i$:

$$
c_i=\sum_{j\sim i}\frac1{\ell_{ij}},
\qquad d_i=\sum_{j\sim i}\frac1{\ell_{ij}^2}.
$$

$$
R_i=\frac{c_i}{d_i}.
$$

For example, if three edges all have length $2$, then $c_i=3/2$ and $d_i=3/4$, so $R_i=2$. More generally, if all incident edges have length $s$, then $R_i=s$, regardless of their number. This is also a weighted average of the incident lengths: the weight of length $\ell$ is proportional to $1/\ell^2$, so shorter edges have greater influence.

The balance equation requires each edge $ij$ to satisfy

$$
\frac{R_i^2+R_j^2}{\ell_{ij}}-R_i-R_j=0.
$$

Since $R_i,R_j>0$, we can write it as

$$
\ell_{ij}=\frac{R_i^2+R_j^2}{R_i+R_j}.
$$

If both endpoint ratios are $s$, the edge must have length $s$. If the ratios are $1$ and $2$, the length must be $(1+4)/(1+2)=5/3$. But we cannot simply prescribe ratios independently: each $R_i$ must also be recovered from the edges around it. The construction must make both directions of this calculation agree.

## Joining $1$, $2$ and $5/3$

Choose a path extending infinitely in both directions, with vertices $\ldots,v_{-1},v_0,v_1,\ldots$. Call it the spine. Attach an infinite binary branch at each $v_n$. Every branch vertex has one parent and two children, so the resulting graph has degree three everywhere.

Set $s_n=2^n$. Give the entire branch at $v_n$, including the edge attaching it to the spine, length $s_n$. Give the spine edge from $v_n$ to $v_{n+1}$ length $(5/3)s_n$. The three lengths around $v_0$ are therefore $5/6,5/3,1$. Their two sums are

$$
c_{v_0}=\frac65+\frac35+1=\frac{14}5,
$$

$$
d_{v_0}=\frac{36}{25}+\frac9{25}+1=\frac{14}5.
$$

Thus $R_{v_0}=1$. Multiplying every incident length by $2^n$ divides $c$ by $2^n$ and $d$ by $2^{2n}$, so it multiplies their ratio by $2^n$. Therefore $R_{v_n}=s_n$ at every spine vertex. Within a branch, the three incident lengths all equal $s_n$, so its vertices also have ratio $s_n$.

Now check each kind of edge. On a branch edge or attachment edge, both endpoint ratios and the edge length equal $s_n$, so the equation holds automatically. On a spine edge, the endpoint ratios are $s_n$ and $2s_n$, requiring exactly the chosen length $(5/3)s_n$. These two cases cover every edge of the infinite tree, rather than just the finite portion we can draw.

The attachment at $v_0$ has length $1$, while the neighboring spine edge has length $5/3$. The whole solution is nonconstant. Yet every junction away from the spine has equal incident lengths. This is how local uniformity can coexist with global variation.

The short film draws the spine, its equal-length branches and the cancellation that preserves each effective length.

::: {.film src="001-balanced-tree"}
A cubic-tree counterexample explains how local balance permits global nonuniformity, with English narration and aligned Chinese and English subtitles.
:::

## The cancellation that makes branching possible

Suppose an existing junction already has ratio $R=c/d$. Add an edge of length $R$. The new sums are

$$
c'=c+\frac1R,
\qquad d'=d+\frac1{R^2}.
$$

Because $c=Rd$, we still have $c'=Rd'$, hence $c'/d'=R$. Adding several such edges has the same effect. Extend each new edge into an entire constant-length branch: every new vertex has ratio $R$, and every new edge satisfies the equation.

This gives an extension principle. Start with any positive solution on a connected, locally finite tree with at least one edge and degree at most $q+1$. Fill the missing neighbors at every vertex to obtain a solution on $T_q$, preserving all original lengths and ratios. A line is one convenient starting point.

The authors also give an explicit family for every integer $q\ge2$. Set $s_n=tr^n$, where $t>0$ and $r>0$ with $r\ne1$, and replace the spine coefficient by

$$
a=\frac{r^2+1}{r+1}.
$$

Attach $q-1$ branches at every spine vertex, each with length $s_n$. The identity $a(r+1)=r^2+1$ makes the ratio calculated at that vertex equal $s_n$. Thus neither degree three nor doubling is essential to the counterexample.

## More freedom than a geometric progression

Huang and colleagues' classification of line solutions allows an independent choice of neighboring length ratio $2$ or $3$ at each step. For example, start with $L_0=1$ and choose $2,3,2$: this gives $L_1=1/2$, $L_2=1/6$ and $L_3=1/12$. Recursion in the negative direction completes a doubly infinite sequence.

Whether the choices repeat periodically or not, the extension principle lifts the line to every $T_q$. If both ratios occur, the spine is no longer one geometric progression. This does not mean arbitrary positive ratios work: $2$ and $3$ satisfy one exact algebraic relation, calculated directly in the technical chapter.

## What fails, and what remains true?

Conjecture 4 in Huang and colleagues' §5.2, printed page 32, says that $T_2$ has no positive nonconstant solution. The cubic example disproves it. Conjecture 3 says that equal incident lengths at one vertex force global constancy. The authors' construction disproves this for every $q\ge2$, even with uniformity at every vertex outside the spine.

A correct global condition is available: for positive solutions on these trees, all edge lengths are constant if and only if all vertex ratios are constant. This requires agreement of $R_i$ throughout the graph. One tidy junction supplies no such information about the other ratios.

The examples have nonconstant curvature too. Here curvature is a number assigned to each edge by the original research, measuring a local feature of the discrete geometry. Under that definition, an interior branch edge in the cubic example has curvature $-2/3$, while an attachment has curvature $-13/21$. The latter is larger. This conclusion comes from the curvature formula, rather than from how bent an illustration looks.

Gubser and collaborators, in a 2016 preprint published in 2017, and later Huang and colleagues, already constructed nonconstant solutions for odd $q$. This family also covers even $q$ and does not require the edges at a vertex to split into two equally sized groups. It demonstrates a failure of local-to-global rigidity without classifying all solutions.

Finally, consider infinity. For $r\ne1$, the scales $tr^n$ approach zero in one direction and grow without bound in the other. Each individual edge remains strictly positive, but there is no common positive lower bound. Setting $r=1$ recovers the constant solution. These examples do not satisfy the asymptotically constant boundary hypothesis in Huang and colleagues' separate uniqueness theorem, so they do not contradict that theorem.

## Read further, or give the talk

[The technical chapter](statements.md) retains the full hypotheses and proofs of all six results in version 2. [The evidence and references appendix](appendix.md) explains the exact Lean correspondence and links to contribution tasks. The public Lean theorem proves the cubic conjecture's negation; its proof constructs the concrete witness above. The parameterized family and subsequent results retain the authors' written proofs here.

The bilingual seminar and speaker notes follow the same mathematical route.

::: {.slides src="seminar"}
An academic talk from a concrete fractional example to branch extension, arbitrary two-choice patterns and precise formalization scope.
:::
