GMT之psmeca绘制震源机制解
#########################

:date: 2013-08-12 16:12
:modified: 2013-06-20
:author: SeisMan
:category: GMT
:tags: GMT命令, 震源机制解, 震源球
:slug: use-psmeca-to-plot-mechanisms
:summary: 用pemeca绘制震源球

.. contents::

写在前面
========

GMT中包含了很多补充包，meca就是其中一个，这个软件包包含了四个命令：pscoupe、psmeca、pspolar和psvelo，主要用于绘制震源机制解、误差椭圆、速度矢量等，这篇博文只介绍其中之一，用于绘制震源球的psmeca命令。

语法
====

::

    psmeca <infiles> -J<params> -R<west>/<east>/<south>/<north>[r]
       -S<format><scale>[/fontsize[/justify/offset/angle/form]]
       [-B<params>] [-C[<pen>][P<pointsize>]]
       [-Ddepmin/depmax] [-E<fill>] [-G<fill>]
       [-H[<nrec>]] [-K] [-L<pen>] [-M] [-N] [-O] [-P] [-r]
       [-Tnplane[/<pen>]] [-U[<just>/<dx>/<dy>/]]
       [-V] [-W<pen>] [-X[a|c|r]<x_shift>[u]] [-Y[a|c|r]<x_shift>[u]]
       [-Z<cpt>] [-z] [-a[size[/Psymbol[Tsymbol]]]
       [-p<pen>] [-t<pen>] [-e<fill>] -g<fill>]
       [-o] [-c<ncopies>] [-:[i|o]]

选项说明
========

-  infiles：一个或多个文件名，文件内包含特定格式的震源机制文件，若未给定文件，则从stdin中读入震源机制解
-  **-J**\ 和\ **-R**\ ：指定地图投影以及地图区域。（本质上，这个命令只绘制震源球，区域地图、地形以及其他都需要使用其他命令绘制。这个命令需要-J和-R的原因在于，通过指定地图投影、绘图尺寸、区域范围等，就可以将唯一的经纬度位置定位在纸上的某一点上。从而保证震源球可以精确得绘制在某个指定位置，而不需要通过-X和-Y去调整位置。这也就是前面所说的pssac和pssac2在地图上绘制地震图的最大区别。）
-  **-S**\ <format><scale>[/fontsize[/justify/offset/angle/form]]：选择震源机制解格式，指定数据文件中每列的含义。关于具体的format放在后面说。scale指定了震级为5的震源球的大小，fontsize等指定了震源球标题的文本属性。默认fontsize为9，offset=0.04；
-  **-B**\ ：设置地图边界的注释和刻度标记间隔
-  **−C**\ [*pen*\ ][\ **P**\ *pointsize*]：在震源机制解文件中会给出地震的经纬度信息。有些时候也可以在特定列（参见具体格式中的newX和newY）给出震源球要放置的经纬度信息（有些情况下不希望震源球把地震的地形信息掩盖）。-C选项在初始位置绘制一个小圆，并绘制一条直线连接小圆和震源球。pen指定直线的属性，pointsize指定圆的大小。默认值线宽=1，颜色=0/0/0,实线；圆大小为0。\ **注意：如果想要将震源球放在地震位置以外的地方，需要将newX和newY设置为新的经纬度值，同时必须有-C选项，震源球才会放在newX和newY指定的位置。**
-  **-D**\ *depmin/depmax*\ ：只绘制某深度范围内的地震
-  **-E**\ *fill*\ 和\ **-G**\ *fill* ：设定震源球的拉伸象限和压缩象限的颜色，默认分别为白和黑。可以指定shade值（0-255）或颜色（rgb）
-  **−L**\ [*pen*\ ]：设置震源球外部轮廓的线条属性，默认为width = 1, color = 0/0/0, texture = solid
-  **-M**\ ：默认震源球大小与震级大小成正比，该选项强制所有震源球大小相同，具体大小由-S给出
-  **-N** ：对地图区域外的震源球也要绘制，默认不绘制。
-  **-r**\ ：在文本周围加上方框
-  **−T**\ [*num\_of\_planes*\ ]：num\_of\_planes可以取0,1,2，分别代表绘制两个节面和只绘制第一个节面、只绘制第二个节面。
-  **-Z**\ *cptfile* ：指定cpt文件，根据数据文件中第三列的值（也就是地震深度）以及cpt文件决定震源球的压缩部分的颜色。
-  **-z ：**\ 覆盖零秩地震矩
-  **−a**\ [*size*/[*P\_axis\_symbol*\ [*T\_axis\_symbol*\ ]]]：计算并绘制P轴和T轴，可以指定大小以及P和T轴的符号，其中符号可以取 (**c**) circle, (**d**) diamond, (**h**) hexagon, (**i**) inverse triangle, (**p**) point, (**s**) square, (**t**) triangle, (**x**) cross，默认是0.2\ **c**/**cc**\ 或0.08\ **i**/**cc**
-  **-e**\ *fill*\ 和\ **-g**\ *fill* ：并-E和-G类似，此处指定P和T轴符号的颜色填充
-  **-o** ：兼容前版的\ **psvelomeca**\ 命令，输入文件中不包含第三列的地震深度
-  **−p**\ [*pen*\ ]和\ **−t**\ [*pen*\ ] ：指定p轴和t轴的线条属性
-  -K，-O，-P，-H，-U，-V，-W，-X，-Y，-：，-c：GMT常见命令选项，参见GMT手册

震源机制解格式-S选项说明
========================

−Sc
---

Harvard CMT格式（现在的Global CMT）

::

    X Y depth strike1 dip1 rake1 strike2 dip2 rake2 mantissa exponent newX newY title

这里给出了两个strike、dip、rake，分别代表两个不同的节面。mantissa和exponent分别代表地震矩的尾数和指数部分（这里地震矩的单位为dyne-cm）。同样scale指定的是震级为5的震源球大小（相当于地震矩为$4.0e-{23} dyne \\cdot cm$，此处mantissa=4.0，exponent=23）。（exponent这里可能有bug，因为当其值为0或者其他比较小的整数时，其震源球反而很大）

−Sa
---

Aki & Richards (1980)约定，根据书中约定的机制解格式。

::

    X Y depth strike dip rake mag newX newY title

其中X和Y为地震经纬度；dep为地震深度，单位为km；strike、dip、rake参照Aki书中的定义，单位为度；mag为震级；newX和newY为放置震源球的经纬度，其值为0，0代表震源球放在地震震中处；title为在震源球上出现的标题。

-Sp
---

::

    X Y depth strike1 dip1 strike2 fault mag newX newY title

其中fault=-1/+1，分别代表正断层和逆断层。

-Sm|d|z
---------

Harvard CMT解，矩阵迹为0

-  m表示绘制地震矩的零迹部分
-  d表示仅绘制地震矩的double couple部分
-  z表示仅绘制地震矩的各向异性部分
-  三个选项的格式相同，不同的选项提取出地震矩中的不同部分，关于地震矩的分解以及具体名词参见相关书籍。

::

    X Y depth mrr mtt mff mrt mrf mtf exp newX newY title

mrr等为地震矩的六个分量，exp代表地震矩的指数部分，例如mtt=2.0，exp=26，则代表实际的$mtt=2.0e-{26}dyne \\cdot cm$。还不清楚r、t、f分别代表哪个方向，可能是东西南北，也可能是大圆路径。

-Sx|y|t
---------

指定主坐标轴的方位，即T、N、P轴

::

    X Y depth Tvalue Tazim Tplunge Nvalue Nazim Nplunge Pvalue Pazim Pplunge exp newX newY title

-  x：根据标准的机制解绘制
-  y：只绘制地震矩的double couple部分
-  z：绘制0迹地震矩
-  这种格式应该不太常用吧

绘图
====

常用的震源机制解来自于Global CMT（\ `http://www.globalcmt.org/CMTsearch.html`_\ ），其可以指定输出类型，满足大多数情况的需要。

这里用的例子如下：

**010176A**\ KERMADEC ISLANDS REGION

.. figure:: http://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/webCMTgif/form?mrr=7.68&mtt=0.09&mpp=-7.77&mrt=1.39&mrp=4.52&mtp=-3.26
   :align: right
   :alt: Meca
   :width: 50 px

::

      Date: 1976/ 1/ 1   Centroid Time:  1:29:53.4 GMT
      Lat= -29.25 Lon=-176.96
      Depth= 47.8   Half duration= 9.4
      Centroid time minus hypocenter time: 13.8
      Moment Tensor: Expo=26  7.680 0.090 -7.770 1.390 4.520 -3.260 
      Mw = 7.3    mb = 6.2    Ms = 0.0   Scalar Moment = 9.56e+26
      Fault plane:  strike=202    dip=30   slip=93
      Fault plane:  strike=18    dip=60   slip=88

将其改写为-Sc所需要的格式为：

::

    -176.96 -29.25 47.8 202 30 93 18 60 88 9.56 26 0 0 010176A

注：在Global CMT选择输出类型Output type时，最好选择GMT psmeca input而不是GMT psvelomeca input，psvelomeca是旧版GMT的命令，两种格式的主要差别在于psvelomeca格式中没有地震深度信息，绘制这种格式的机制解需要额外添加-o选项。

另外GMT psmeca input类型给出的结果如下：

::

    -176.96 -29.25 48 7.68 0.09 -7.77 1.39 4.52 -3.26 26 X Y 010176A

其对应的格式是-Sm，注意与-Sc的区别。格式中的newX和newY被替换成了X和Y，这个在程序中好像会被认为是0值，因而可以正常运行。

最简单的图
----------

.. code-block:: bash

 #!/bin/bash
 PS=meca1.ps

 pscoast -Rg -JQ10i -B60/30 -A10000 -Wthin -G200 -K > ${PS}
 psmeca -R -J -Sc1 -W1p -K -O << EOF >> ${PS}
 -176.96 -29.25 47.8 202 30 93 18 60 88 9.56 26 0 0 010176A
 EOF

效果图如下，这里与GCMT给的结果不同，因为使用strike、rake、dip所决定的double couple地震矩仅仅只是地震矩的一部分。

.. figure:: http://ww1.sinaimg.cn/large/c27c15bejw1e7aovu0300j20r70ei0ui.jpg
   :alt: meca
   :width: 700 px

一个稍稍复杂的版本
------------------

.. code-block:: bash

 #!/bin/bash
 PS=meca2.ps

 pscoast -Rg -JQ10i -B60/30 -A10000 -Wthin -G200 -K > ${PS}
 #plot mechanism
 psmeca -R -J -Sc1/12/0.2 -C0.5pP2p -Egrey -Gred -L1p -W1p -K -O << EOF >> ${PS}
 -176.96 -29.25 47.8 202 30 93 18 60 88 9.56 26 -160 -10 010176A
 EOF

效果如下：

.. figure:: http://ww2.sinaimg.cn/large/c27c15bejw1e7aowxafxbj20r30e5gnh.jpg
   :alt: meca
   :width: 700 px

最后说明
========

这个命令其实还是比较简单的，从第一张图来看，默认效果已经很不错了，关键还是要对地震矩的概念及地震矩分解有更进一步的了解。一个不错的文章是：

Jost M L, Herrmann R B. A student’s guide to and review of moment tensors[J]. Seismological Research Letters, 1989, 60(2): 37-57.

修订历史
=========

-  2013-05-10：初稿；
-  2013-05-14：在例子中简单解释了GCMT的默认GMT输入格式。
-  2013-06-05：若要将震源球移动到新位置，需要设定newX和newY为新的经纬度，且给出-C选项。
-  2013-06-20：去除了第一个例子中的-T0选项。

.. _`http://www.globalcmt.org/CMTsearch.html`: http://www.globalcmt.org/CMTsearch.html
