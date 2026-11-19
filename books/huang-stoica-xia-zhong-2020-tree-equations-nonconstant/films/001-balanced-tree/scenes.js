/* 原论文第 2 版：Theorem 1、Corollary 2、Lemma 3。
   图只表示邻接关系；边长由标签给定。所有时间来自共享引擎与旁白。 */
'use strict';
function heading(en, zh) {
  txt(en, 110, 205, {size:47, fam:F.disp, w:700, c:C.white});
  txt(zh, 112, 248, {size:28, fam:F.zh, c:C.cyan});
}
function lineSegment(x1,y1,x2,y2,col=C.cyan,a=1,w=5) {
  ctx.save(); ctx.globalAlpha=a; ctx.strokeStyle=col; ctx.lineWidth=w;
  ctx.beginPath(); ctx.moveTo(x1,y1); ctx.lineTo(x2,y2); ctx.stroke(); ctx.restore();
}
function label(s,x,y,o={}) { txt(s,x,y,Object.assign({size:34,fam:F.math,align:'center',c:C.white},o)); }
function tree(a=1, branches=1, labels=1, highlight=false) {
  const xs=[400,960,1520];
  lineSegment(180,440,400,440,C.dim,a);
  lineSegment(400,440,960,440,C.cyan,a);
  lineSegment(960,440,1520,440,C.cyan,a);
  lineSegment(1520,440,1740,440,C.dim,a);
  for(let k=0;k<3;k++) {
    const x=xs[k], col=highlight&&k===1?C.now:C.mag;
    dot(x,440,14,'c',a); label(['v₋₁','v₀','v₁'][k],x,399,{a});
    const ba=a*branches;
    lineSegment(x,440,x,590,col,ba);
    lineSegment(x,590,x-120,710,col,ba); lineSegment(x,590,x+120,710,col,ba);
    lineSegment(x-120,710,x-170,775,col,ba); lineSegment(x-120,710,x-70,775,col,ba);
    lineSegment(x+120,710,x+70,775,col,ba); lineSegment(x+120,710,x+170,775,col,ba);
    dot(x,590,12,'c',ba);dot(x-120,710,10,'c',ba);dot(x+120,710,10,'c',ba);
    label(['1/2','1','2'][k],x+48,530,{a:ba*labels,c:col});
    label('⋯',x-120,818,{a:ba}); label('⋯',x+120,818,{a:ba});
  }
  label('5/6',680,420,{a:a*labels});label('5/3',1240,420,{a:a*labels});
}
SCENES.question = S => {
  heading('Can local balance force global equality?', '局部平衡，能否迫使整体相同？');
  panel(100,285,1720,560,1,C.cyan);
  tree(at(S,1,0.8),at(S,2,0.8),at(S,2,0.8));
  label('schematic: labels give lengths',960,330,{size:25,c:C.dim});
};
SCENES.equation = S => {
  heading('The ratio must agree with the edges', '边决定比值，比值还要与边相容');
  panel(100,300,780,530,1,C.cyan,'AT ONE JUNCTION');
  panel(940,300,880,530,1,C.cyan,'ON EACH EDGE');
  label('c = Σ 1/ℓ',490,430,{size:54});
  label('d = Σ 1/ℓ²',490,525,{size:54});
  label('R = c/d',490,630,{size:60,c:C.cyan});
  label('ℓ = (Rᵢ² + Rⱼ²)/(Rᵢ + Rⱼ)',1380,460,{size:42,a:at(S,2,0.5)});
  label('Rᵢ = 1     Rⱼ = 2',1380,585,{size:47,a:at(S,2,0.5)});
  label('ℓ = (1 + 4)/(1 + 2) = 5/3',1380,700,{size:42,c:C.now,a:at(S,2,0.8)});
  label('three equal edges of length 2 → R = 2',490,760,{size:28,a:at(S,1,0.6)});
};
SCENES.spine = S => {
  heading('One spine, infinitely many branches', '一条主干，接上无限分支');
  panel(100,285,1720,560,1,C.cyan);
  tree(at(S,0,0.8),at(S,1,1.1),at(S,2,0.8));
  label('branch scale sₙ = 2ⁿ; spine length = (5/3)sₙ',960,330,{size:33,a:at(S,2,0.8)});
};
SCENES.check = S => {
  badgeQ(S, [[0,'Both sums','computed']]);
  heading('Two checks cover the infinite tree', '两种边的检验，覆盖整个无限树');
  panel(100,300,780,535,1,C.cyan,'AT v₀: 5/6, 5/3, 1');
  label('c = 6/5 + 3/5 + 1 = 14/5',490,415,{size:38});
  label('d = 36/25 + 9/25 + 1',490,500,{size:36});
  label('= 14/5',490,555,{size:42});
  label('R₀ = 1     Rₙ = 2ⁿ',490,685,{size:48,c:C.cyan,a:at(S,1,0.8)});
  panel(940,300,880,535,1,C.cyan,'EDGE EQUATIONS');
  label('branch + attachment',1380,400,{size:34,a:at(S,2,0.6)});
  label('2s²/s − 2s = 0',1380,480,{size:48,a:at(S,2,0.6)});
  label('spine',1380,585,{size:34,a:at(S,2,0.6)});
  label('(s² + 4s²)/(5s/3) − 3s = 0',1380,665,{size:40,a:at(S,2,0.6)});
  label('1 ≠ 5/3: nonconstant',1380,770,{size:42,c:C.now,a:at(S,3,0.8)});
};
SCENES.extension = S => {
  badgeQ(S, [[0,'general mechanism','argued']]);
  heading('Add branches; keep the same ratio', '增加分支，保持原比值');
  panel(100,300,680,540,1,C.argued,'FILL MISSING NEIGHBORS');
  dot(440,480,20,'c');label('R',440,435,{size:52});
  lineSegment(160,480,440,480,C.dim);lineSegment(440,480,680,480,C.dim);
  const a=at(S,0,0.8);
  lineSegment(440,480,440,650,C.mag,a);dot(440,650,15,'c',a);
  lineSegment(440,650,320,770,C.mag,a);lineSegment(440,650,560,770,C.mag,a);
  label('each new edge: R',440,815,{size:28,c:C.mag,a});
  panel(840,300,980,540,1,C.argued,'THE CANCELLATION');
  label('c′ = c + m/R',1330,425,{size:53,a:at(S,1,0.5)});
  label('d′ = d + m/R²',1330,520,{size:53,a:at(S,1,0.5)});
  label('c = Rd  ⇒  c′ = Rd′',1330,640,{size:51,c:C.argued,a:at(S,1,0.8)});
  label('R′ = R',1330,755,{size:66,c:C.cyan,a:at(S,2,0.7)});
};
SCENES.scope = S => {
  // 绿色仅用于旁白明确陈述的三正则树全称常值命题之否定。
  badgeQ(S, [[0,'public Lean theorem','lean'],[1,'written paper','argued']]);
  heading('The cubic constancy conjecture is false', '三正则树常值猜想为假');
  panel(100,300,1720,190,1,C.cyan);
  label('Cubic constancy conjecture: false',960,382,{size:53,c:C.cyan});
  label('fixed infinite witness: q = r = 2, t = 1',960,445,{size:34});
  panel(100,530,1720,300,at(S,1,0.7),C.argued);
  label('Written family: q ≥ 2, sₙ = trⁿ',960,610,{size:48,a:at(S,1,0.7)});
  label('t > 0, r > 0, r ≠ 1',960,680,{size:43,a:at(S,1,0.7)});
  label('one end → 0; the other → ∞',960,755,{size:41,c:C.dim,a:at(S,2,0.7)});
  label('Ma & Zhang · version 2 · DOI 10.5281/zenodo.23935004',960,280,{size:26,c:C.dim});
};
FILM.poster = () => {
  heading('Locally balanced, globally nonuniform', '局部平衡，整体不均匀');
  panel(100,285,1720,560,1,C.cyan);
  tree(1,1,1,true);
  label('Equal branches; changing spine scales',960,900,{size:39,c:C.white});
  label('Haobo Ma · Wenlin Zhang · version 2',960,970,{size:28,c:C.dim});
};
