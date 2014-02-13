Doule Couple辐射花样可视化
#####################################################
:date: 2013-09-02 00:09
:author: SeisMan
:category: Mathematica, 地震学软件
:tags: 震源机制解, 震源球
:slug: doule-couple-radition-pattern

Aki & Richards (1980) P118
给出了远场P、SV、SH波的辐射花样。一直想将辐射花样画出来，以更好的理解不同震源机制的辐射花样。无奈各种绘图软件都只知皮毛。

下面给出用Mathematica写的两个辐射花样可视化的程序，可以下载封装好的cdf文件（用免费的\ `cdf-player`_\ 打开）或者nb源文件（用商业软件Mathematica打开）。

---------------------------------------------华丽的分割线---------------------------------------------------------------

网址：\ `http://demonstrations.wolfram.com/RadiationPatternForDoubleCoupleEarthquakeSources/`_
 下载：\ `cdf文件`_ `nb源代码`_

效果图如下，可以调节strike、rake、dip的值，选择波类型，来获得相应的辐射花样。（有些复杂，没怎么看明白。）
 |image0|

---------------------------------------------华丽的分割线---------------------------------------------------------------

网址：\ `http://demonstrations.wolfram.com/EarthquakeFocalMechanism/`_
 下载：\ `cdf文件`_ `nb源代码`_

效果图如下，这张图实际是根据P波初动绘制震源球，算是上图的一个简化版，通过修改strike、rake、dip的值，可以很清晰地看到震源球的断层面的移动过程，有助于锻炼“看震源球确定断层机制”的能力。
 |image1|

.. _cdf-player: http://www.wolfram.com/cdf-player/
.. _`http://demonstrations.wolfram.com/RadiationPatternForDoubleCoupleEarthquakeSources/`: http://demonstrations.wolfram.com/RadiationPatternForDoubleCoupleEarthquakeSources/
.. _cdf文件: http://demonstrations.wolfram.com/RadiationPatternForDoubleCoupleEarthquakeSources/RadiationPatternForDoubleCoupleEarthquakeSources.cdf
.. _nb源代码: http://demonstrations.wolfram.com/data/006575/0009/RadiationPatternForDoubleCoupleEarthquakeSources/RadiationPatternForDoubleCoupleEarthquakeSources-source.nb
.. _`http://demonstrations.wolfram.com/EarthquakeFocalMechanism/`: http://demonstrations.wolfram.com/EarthquakeFocalMechanism/
.. _cdf文件: http://demonstrations.wolfram.com/EarthquakeFocalMechanism/EarthquakeFocalMechanism.cdf
.. _nb源代码: http://demonstrations.wolfram.com/data/006369/0010/EarthquakeFocalMechanism/EarthquakeFocalMechanism-source.nb

.. |image0| image:: http://ww3.sinaimg.cn/large/c27c15bejw1e87cuyd86oj20ev0gtwf1.jpg
.. |image1| image:: http://ww4.sinaimg.cn/large/c27c15bejw1e87d0195hij20d00hk3za.jpg
