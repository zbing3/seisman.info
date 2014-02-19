GMT 绘制中国边界需要注意的问题汇总
##################################

:date: 2013-12-30 22:17
:author: SeisMan
:category: GMT
:slug: gmt-china-boundary-problems

.. contents::

在中国，发表论文若地图中涉及到中国边界时，图件需要上报进行审核。具体审核哪些内容，我没有细致地找过相关文件和制图要求。

一直听说GMT绘制的中国边界有问题，无法直接发表，需要做额外的处理。这篇文章总结一下GMT在绘制中国边界时需要注意的一些问题。

我没有绘制中国边界的需求，所以没有认真研究过究竟需要注意哪些问题，下面的问题列表还需要更多的补充和修订。

九段线数据
==========

GMT自带的数据中没有九段线数据，因而在绘制中国边界时需要额外提供九段线数据。目前没有找到比较官方的九段线数据。

边界问题
========

前面的系列博文（\ `博文1`_\ 、\ `博文2`_\ 、\ `博文3`_\ 、\ `博文4`_\ ）中介绍了如何利用DCW数据和公开的行政区划数据绘制省界和国界等，这两种方法绘制的边界都存在问题，无法直接用于发表。

#. 麦克马洪线
#. 新疆地区中印边界

如何绘制中国边界，这个问题很重要，不过目前对这个问题没太大的兴趣。

关于边界差异的细节可以参考\ `Altimetry 技术空间`_\ 博客里的\ `这篇博文`_\ 中的第一张图。

未完待续。。

欢迎补充。。

.. _博文1: http://seisman.info/introduction-to-dcw-gmt5.html
.. _博文2: http://seisman.info/usage-of-dcw-data.html
.. _博文3: http://seisman.info/gmt-map-coloring.html
.. _博文4: http://seisman.info/china-administrative-areas-data.html
.. _Altimetry 技术空间: http://hi.baidu.com/yangleir
.. _这篇博文: http://hi.baidu.com/yangleir/item/09dc00074c9b6d35a3332a33
