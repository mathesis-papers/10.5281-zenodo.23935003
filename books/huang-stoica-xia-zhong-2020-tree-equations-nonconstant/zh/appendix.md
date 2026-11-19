# 证据与文献

## Lean 声明具体检查什么

[固定版本的 Lean 证明](lean:D5/S3/Geometry/DiscreteGravity/TreeEquationsNonconstantRefutation.result)验证了三正则树反例。下表区分这一结论与更广的书面定理。

下面的声明证明 [@cubic-negation] 中三正则树全称常值命题的否定。其证明构造一个固定的无限反例，而非有限邻域样本。假设要求边上正性、对称性，图局部有限且为树，每点度数三，所有边残差为零；没有边界条件或统一正下界。Lean 命题还显式包含可判定邻接关系。


倒数和、比值与残差的定义在本章适用域上与技术章一致。Lean 的实数除法是全定义的，但这里的正性与非空有限邻居集保证 $c_i,d_i>0$，不会引入额外的零分母情形。非边上的长度函数值不参与断言。图、具体长度、比值计算及残差检查是公开证明内部的私有构造；公开结论本身是 `¬ claim`。

| 原论文结果 | 精确对应范围 |
| --- | --- |
| Theorem 1：任意 $q,t,r$ 及显式比值 | 公开证明内部给出 $q=r=2,t=1$ 的固定情形，不陈述参数家族。 |
| Corollary 2：两个猜想及任意 $q\ge2$ | 公开定理给出三正则树常值断言的否定；所有度数的等长星形反例需要更广的声明。 |
| Lemma 3：任意输入树的扩张 | 有书面证明；所查 DiscreteGravity 模块没有对应公开陈述。 |
| Corollary 4：任意双向二选一序列 | 有书面证明，承接早先的直线分类；本讲解还给出直接代数检验。 |
| Corollary 5：整体常值的充要条件 | 两个方向都有书面证明，与单个不等长反例不同。 |
| Corollary 6：两种曲率公式及严格不等式 | 有书面证明；公开三正则树否定命题不含曲率结论。 |

无限范围的陈述依靠完整证明；有限有理数检查用于展示若干具体输入。

## 贡献一个精确的缺失声明

现有书面证明已经给出数学结论。以下共享请求说明仍需完成的形式化工作：

- [Theorem 1, Section 1：Geometric-spine solutions on every regular tree](https://github.com/the-omega-institute/trureturing-requests/issues/125)。
- [Corollary 2, Section 1：Equal-star rigidity fails on every regular tree](https://github.com/the-omega-institute/trureturing-requests/issues/126)。
- [Lemma 3, Section 2：Extend a tree solution by constant-length branches](https://github.com/the-omega-institute/trureturing-requests/issues/127)。
- [Corollary 4, Section 2：Arbitrary two-choice spine patterns on regular trees](https://github.com/the-omega-institute/trureturing-requests/issues/128)。
- [Corollary 5, Section 2：Constant lengths if and only if constant vertex ratios](https://github.com/the-omega-institute/trureturing-requests/issues/129)。
- [Corollary 6, Section 3：Nonconstant curvature of geometric-spine solutions](https://github.com/the-omega-institute/trureturing-requests/issues/130)。

可在对应共享问题中协调证明范围，并依照[贡献指南](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)提交证明。请保留原结果及早先文献的数学归属。

## 论文身份与引用

引用第 2 版请使用 DOI **10.5281/zenodo.23935004**；概念 DOI **10.5281/zenodo.23935003** 指向版本集合。论文采用 CC BY 4.0 许可。

## 参考文献

1. Haobo Ma and Wenlin Zhang. *Counterexamples to Conjectures 3 and 4 of Huang, Stoica, Xia and Zhong (arXiv:2006.06716v1, Section 5.2, printed page 32)*, version 2 (2026). [精确版本 DOI](https://doi.org/10.5281/zenodo.23935004). [版本集合](https://doi.org/10.5281/zenodo.23935003). CC BY 4.0.
2. A. Huang, B. Stoica, X. Xia and X. Zhong. *Bounds on the Ricci curvature and solutions to the Einstein equations for weighted graphs* (2020). [arXiv:2006.06716v1](https://arxiv.org/abs/2006.06716v1). 方程 (3.1) 给出树方程；Theorem 10，§5.1，印刷第 28–29 页给出直线分类；Conjectures 3–4，§5.2，印刷第 32 页是这里否定的猜想；方程 (4.10)，印刷第 13 页定义所用曲率。Definition 13 与 Theorem 2 另有渐近常值边界条件。
3. S. S. Gubser, M. Heydeman, C. Jepsen, M. Marcolli, S. Parikh, I. Saberi, B. Stoica and B. Trundy. *Edge length dynamics on graphs with applications to $p$-adic AdS/CFT*. J. High Energy Phys. **2017**, 157 (2017). [DOI](https://doi.org/10.1007/JHEP06(2017)157); [arXiv:1612.09580v1](https://arxiv.org/abs/1612.09580v1), §5，方程 (97)–(99)：先前的奇数 $q$ 构造。
4. S. Bai, H. Cheng and B. Hua. *Discrete Einstein metrics on trees*, [arXiv:2604.22449v3](https://arxiv.org/abs/2604.22449v3) (2026), §1. 原论文引用其有限树上常曲率度量研究，所讨论问题不同。
5. H. Cheng. *Positive-Curvature Discrete Einstein Metrics on Trees*, [arXiv:2605.20862v2](https://arxiv.org/abs/2605.20862v2) (2026), §1. 同样须区分常曲率问题与这里的树方程。
