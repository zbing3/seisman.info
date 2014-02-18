体力与等效体力
##############

:date: 2013-09-16 00:07
:author: SeisMan
:category: 地震学基础
:slug: body-force-equivalents

地震学里最基本的运动方程是 $$ \\rho \\ddot{u\_i} = \\sigma\_{ij,j} + f\_i $$

其中$f\_i$是体力项，最常见的体力是重力。

除非是研究地球的自由震荡，在一般的地震波传播问题中，重力都是可忽略的，因而运动方程简化为：

$$ \\rho \\ddot{u\_i} = \\sigma\_{ij,j} $$

断层的破裂过程（即震源的激发过程）可以认为其在源区导致局部的本构关系发生变化。其中$\\sigma\_{ij}$是真实的应力场，而$s\_{ij}$是根据原本构关系计算得到的应力场。

定义

$$ f\_i \\equiv (\\sigma\_{ij}-s\_{ij})\_{,j} $$

此时运动方程重新变成

$$ \\rho \\ddot{u\_i} = \\sigma\_{ij,j} + f\_i $$

$s\_{ij}$是根据原本构关系计算得到的应力场，因而其在整个空间内是连续的。注意这里的$f\_i$已经不再是体力了，而是从被修改的本构关系中分解出的体力项，因而$f\_i$仅仅存在于震源区的一个点或者断层面上。

根据Aki & Richards (1980)中的表示定理：

.. figure:: http://ww2.sinaimg.cn/large/c27c15bejw1e8n0zkp6m9j20cx0453ym.jpg
   :align: center
   :alt: 

位移分为三项，第一项为体力引起的位移，这一项在波传播中可忽略；

第二项是位移不连续引起的位移，其等效体力为

|image0|

第三项是应力不连续引起的位移，其等效体力为

|image1|

地震学研究中常用的源是位错源，即第二项。

因而很多文献中的波动方程，$f\_i$都不是体力项，而是等效体力项。

参考文献：

1. Julian, B. R., Miller, A. D., & Foulger, G. R. (1998). Non‐double‐couple earthquakes 1. Theory. Reviews of Geophysics, 36(4), 525-549.

.. |image0| image:: http://ww1.sinaimg.cn/large/c27c15bejw1e8n155usryj20ao01bt8k.jpg
.. |image1| image:: http://ww2.sinaimg.cn/large/c27c15bejw1e8n15gefzgj209s016dfo.jpg
