# 精确陈述与完整证明

先构造正则树并验证每条边的方程，再证明添加等长分支的扩张原则。其余结论由这个构造及原文的直线解分类推出。

## 方程及适用范围

$H$ 为连通、局部有限、至少有一条边的简单树，边长 $\ell_{ij}=\ell_{ji}>0$。每个顶点至少有一个邻居，故下面的有限和严格为正：

$$
\begin{aligned}
c_i&=\sum_{j\sim i}\ell_{ij}^{-1},\\
d_i&=\sum_{j\sim i}\ell_{ij}^{-2},\\
R_i&=c_i/d_i>0.
\end{aligned}
$$

在树中，相邻顶点之间的唯一简单路径就是这条边；任意其他有限游走删去回头段后长度变小。因此最短路径长度就是 $\ell_{ij}$。Huang 等人的方程 (3.1) 在这里化为

$$
\mathcal E_{ij}=\frac{R_i^2+R_j^2}{\ell_{ij}}-R_i-R_j=0.
$$

本章不加无穷远边界条件。记 $T_q$ 为无限的 $(q+1)$-正则树。

## 等比主干家族

::: {.theorem #geometric-family title="等比主干家族" status="written-proof" proof="pf-geometric-family" doi="10.5281/zenodo.23935004" source="Theorem 1, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/125" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s1"}
给定整数 $q\ge2$、$t>0$ 以及实数 $r>0$、$r\ne1$，令

$$
s_n=tr^n\quad(n\in\mathbb Z),
\qquad a=\frac{r^2+1}{r+1}.
$$

在双向无限主干 $(v_n)$ 上给 $v_nv_{n+1}$ 长度 $as_n$；在每个 $v_n$ 接 $q-1$ 棵互不相交的有根 $q$ 叉树，每棵分支的所有边（含连接边）都长 $s_n$。这给出 $T_q$ 上的正的不等长解，且 $v_n$ 及接在它上面的每个分支顶点都有 $R_i=s_n$。
:::

::: {.proof #pf-geometric-family}
每棵分支用字母表 $\{1,\ldots,q\}$ 上的有限词标记顶点，空词通过一条边连接到 $v_n$，每个词连接它的 $q$ 个单字母延长。不同 $n$、不同分支使用不同副本。主干顶点有两个主干邻居和 $q-1$ 个分支邻居；分支顶点有一个父顶点和 $q$ 个子顶点。故每点度数恰为 $q+1$，图简单且局部有限。沿父边有限步可到主干，故连通。分支与主干各自无环，且每个分支只有一个连接口，不能借主干形成环。因此这确为 $T_q$ 的一个实现。

所有长度均正，且按无向边赋值所以对称。$v_n$ 的入射长度为 $as_n/r$、$as_n$ 及 $q-1$ 个 $s_n$，因而

$$
c_{v_n}=s_n^{-1}\left(\frac{r+1}{a}+q-1\right),
$$

$$
d_{v_n}=s_n^{-2}\left(\frac{r^2+1}{a^2}+q-1\right).
$$

由 $a(r+1)=r^2+1$，两个括号相同且为正，故 $R_{v_n}=s_n$。分支顶点所有 $q+1$ 条入射边均长 $s_n$，故 $c_i=(q+1)/s_n$，$d_i=(q+1)/s_n^2$，同样有 $R_i=s_n$。

分支内部边与连接边的两端比值及边长都为 $s_n$，其残差为 $2s_n^2/s_n-2s_n=0$。主干边两端的比值为 $s_n$ 与 $rs_n$，故

$$
\mathcal E_{v_nv_{n+1}}
=s_n\left(\frac{1+r^2}{a}-1-r\right)=0.
$$

所有边已被覆盖；残差对端点交换对称。最后，$v_0$ 的连接边长 $t$，下一条主干边长 $at$，而

$$
a-1=\frac{r(r-1)}{r+1}\ne0.
$$

故解不等长。
:::
::: {.corollary #conjecture-refutations title="原猜想的反例" status="written-proof" proof="pf-conjecture-refutations" doi="10.5281/zenodo.23935004" source="Corollary 2, Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/126" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s2"}
Huang 等人 §5.2、印刷第 32 页的猜想 4 为假。对每个 $q\ge2$，同页的猜想 3 在 $T_q$ 上为假；即使要求双向无限路径外的每个顶点都有等长入射边，结论仍不成立。
:::

::: {.proof #pf-conjecture-refutations}
取 [@geometric-family] 的 $q=r=2$、$t=1$，即得到 $T_2$ 的正的不等长解，否定猜想 4。对任意 $q\ge2$，取例如 $r=2,t=1$：每个主干顶点至少接一个分支，每个主干外顶点的入射边均等长，而整个解不等长，否定猜想 3。
:::

### 公开 Lean 定理所陈述的精确结论

下面单独陈述公开声明的逻辑形式。它与上面的全参数推论不同。

::: {.theorem #cubic-negation title="三正则树常值断言的否定" lean="D5/S3/Geometry/DiscreteGravity/TreeEquationsNonconstantRefutation.result" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s2"}
以下全称断言为假：局部有限的三正则树上，若边长对称且严格为正，并且每条边都满足局部方程，那么所有边长必相等。
:::

::: {.proof #pf-cubic-negation}
公开证明在顶点集 $\mathbb Z\sqcup(\mathbb Z\times\mathrm{List}(\mathrm{Bool}))$ 上构造 $q=r=2,t=1$ 的树。整数部分为主干；布尔有限词给出每棵二叉分支。证明分别核对局部有限性、度数三、连通无环、正性和对称性，算出两类顶点的比值 $2^n$，再检验所有边的残差为零。最后，连接边长 $1$ 而相邻主干边长 $5/3$，与共同常值矛盾。公开定理的结论是上述全称命题的否定；具体构造作为其证明的内部对象出现。
:::

## 补充分支的扩张原则

::: {.lemma #branch-extension title="保留原比值的扩张" status="written-proof" proof="pf-branch-extension" doi="10.5281/zenodo.23935004" source="Lemma 3, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/127" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s3"}
设整数 $q\ge2$，$H$ 为连通、局部有限、有至少一条边且所有度数不超过 $q+1$ 的树。$H$ 上的任意正长度解都能扩张成 $T_q$ 上的正长度解，保留原有边长及所有原顶点比值。在 $i\in H$ 处接 $m_i=q+1-\deg_H(i)$ 棵互不相交的有根 $q$ 叉树，每棵新分支（含连接边）的所有边长均为原比值 $R_i$。
:::

::: {.proof #pf-branch-extension}
$H$ 连通且非平凡，所以每个原顶点的度数至少为 $1$，从而 $c_i,d_i,R_i>0$。$m_i$ 是非负整数；若 $m_i=0$，该点不增加分支。用上面的有限词方法造新分支并保持各副本不交。新图连通无环，原顶点度数补足为 $q+1$，每个新顶点有一个父顶点和 $q$ 个子顶点，也有度数 $q+1$，故为 $T_q$。

原顶点的新和为

$$
c'_i=c_i+\frac{m_i}{R_i},
\qquad d'_i=d_i+\frac{m_i}{R_i^2}.
$$

由 $c_i=R_i d_i$ 得

$$
R_i d'_i=R_i d_i+\frac{m_i}{R_i}=c'_i.
$$

$d'_i>0$，所以 $R'_i=R_i$。新分支中每个顶点的所有入射边长均为 $R_i$，其比值也为 $R_i$。原边的长度和端点比值均不变，故原方程仍成立。每条新边，包括连接边，的残差均为 $2R_i^2/R_i-2R_i=0$，证明完毕。
:::
::: {.corollary #two-choice-patterns title="任意二选一主干模式" status="written-proof" proof="pf-two-choice-patterns" doi="10.5281/zenodo.23935004" source="Corollary 4, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/128" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s4"}
固定整数 $q\ge2$、任意双向序列 $b_n\in\{2,3\}$ 以及 $L_0>0$。用 $L_{n-1}/L_n=b_n$ 确定所有正的主干边长 $L_n$，其中 $L_n$ 是边 $v_nv_{n+1}$ 的长度。存在以这些边为主干的 $T_q$ 解；主干外每个顶点入射边等长，整个解不等长。若 $2$、$3$ 两种选择都出现，则主干边长不是一条等比数列。
:::

::: {.proof #pf-two-choice-patterns}
正方向用除法、负方向用乘法从 $L_0$ 递推，因此每个整数位置有唯一正值。这是 Huang 等人 Theorem 10（§5.1，印刷第 28–29 页）中取参数 $2$ 的直线解：另一允许比值为 $(2+1)/(2-1)=3$。为使这里的依赖完整，也可直接验证这个特例。

在直线顶点 $v_n$，两条入射边长是 $b_nL_n$ 与 $L_n$，故

$$
R_n=L_n\frac{b_n(b_n+1)}{b_n^2+1}=\frac65 L_n,
$$

最后一个等号对 $b_n=2,3$ 都成立。在边 $v_nv_{n+1}$ 上，令 $b=b_{n+1}$，则 $L_{n+1}=L_n/b$。因此

$$
\begin{aligned}
\mathcal E_{n,n+1}
&=L_n\Big[\frac{36}{25}(1+b^{-2})\\
&\qquad-\frac65(1+b^{-1})\Big]\\
&=0
\end{aligned},
$$

因为括号乘以 $25b^2$ 后变成

$$
\begin{aligned}
&36(b^2+1)-30(b^2+b)\\
&\qquad=6(b-2)(b-3)=0.
\end{aligned}
$$

所以任意、包括非周期的二选一序列均给出直线解。所有比值至少为 $2$，故 $L_n$ 随 $n$ 严格递减而不常值。应用 [@branch-extension]，在每个直线顶点补 $q-1$ 棵分支，原边长与不等长性保留，主干外入射边等长。若序列含两种比值，则相邻长度之比不恒定，排除单一等比数列。
:::
::: {.corollary #constant-ratios title="常值边长与常值比值等价" status="written-proof" proof="pf-constant-ratios" doi="10.5281/zenodo.23935004" source="Corollary 5, Section 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/129" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s5"}
在连通、局部有限且至少有一条边的树上，一个正长度解的所有边长相同，当且仅当所有顶点比值 $R_i$ 相同。
:::

::: {.proof #pf-constant-ratios}
若所有 $R_i=s$，则每个顶点非孤立和正性保证 $s>0$。每条边的方程为 $2s^2/\ell_{ij}-2s=0$，除以 $2s$ 得 $\ell_{ij}=s$。反之，若所有边长为 $s>0$，每个顶点度数为正且有限，故

$$
c_i=\frac{\deg(i)}s,
\qquad d_i=\frac{\deg(i)}{s^2},
$$

从而 $R_i=s$。两个方向均成立。
:::

## 曲率与边界

采用 Huang 等人的方程 (4.10)，印刷第 13 页：

$$
K_{ij}=\frac2{\ell_{ij}^2}\left(\frac1{d_i}+\frac1{d_j}\right)
-\frac{R_i+R_j}{\ell_{ij}}.
$$

::: {.corollary #nonconstant-curvature title="等比主干的曲率不恒定" status="written-proof" proof="pf-nonconstant-curvature" doi="10.5281/zenodo.23935004" source="Corollary 6, Section 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/130" mathesis="collected:huang-stoica-xia-zhong-2020-tree-equations-nonconstant:2:s6"}
[@geometric-family] 中每个不等长解都有不恒定的树曲率。令 $B=q-1+(r+1)^2/(r^2+1)$，则分支内部边及连接边分别有

$$
K_{\mathrm{branch}}=\frac4{q+1}-2,
$$

$$
K_{\mathrm{attach}}=\frac2B+\frac2{q+1}-2.
$$

且 $K_{\mathrm{attach}}>K_{\mathrm{branch}}$。在 $q=r=2$ 时，两值分别为 $-2/3$ 和 $-13/21$。
:::

::: {.proof #pf-nonconstant-curvature}
主干顶点有 $d_i=B/s_n^2$，分支顶点有 $d_i=(q+1)/s_n^2$。分支内部边的两端均为后一种顶点；连接边的一端为前一种，另一端为后一种。两类边的长度与两端比值均为 $s_n$，代入曲率公式即得所列两式。

由 $(r-1)^2>0$ 得 $(r+1)^2<2(r^2+1)$，故 $0<B<q+1$。因此

$$
K_{\mathrm{attach}}-K_{\mathrm{branch}}
=\frac2B-\frac2{q+1}>0.
$$

$q\ge2$ 保证两类边都存在。$q=r=2$ 时 $B=1+9/5=14/5$，代入得 $K_{\mathrm{branch}}=4/3-2=-2/3$ 及 $K_{\mathrm{attach}}=5/7+2/3-2=-13/21$。
:::

当 $r=1$ 时，同样的公式给 $a=1$、$s_n=t$，恢复等长解，曲率差也为零；这是被不等长性假设排除的等号情形。当 $r>1$，$s_n$ 在 $n\to-\infty$ 时趋于零、$n\to+\infty$ 时趋于无穷；$0<r<1$ 时方向相反。这只是等比数列的极限，不涉及无穷和或交换极限。故这些家族不满足 Huang 等人 Definition 13 与 Theorem 2 的渐近常值边界条件。

在主干顶点，$as_n/r$、$as_n$ 与 $s_n$ 在 $r\ne1$ 时两两不同：$a\ne1$ 已证；$a/r=1$ 会给 $r^2+1=r(r+1)$，从而 $r=1$；前两者相等也会给 $r=1$。因此它们不属于原文 Theorems 11–12 的半半分组假设。原文 Remark 12 已有奇数 $q$ 的非半半例子；这里还覆盖所有偶数 $q\ge2$。任意尺度模式的一般分类仍不由本章得到。
