震中距、方位角和反方位角的计算
#####################################################
:date: 2013-07-03 01:00
:author: SeisMan
:category: 地震学软件
:slug: calculate-dist-az-baz

给定震中经纬度以及球面上任意一点（一般是台站）的经纬度，计算震中距、方位角以及反方位角。这是地震学的一个基本问题。

名词解释
~~~~~~~~

-  震中距：\ **地面**\ 上任意一点到\ **震中**\ 的球面距离；
-  方位角：震中到台站的连线与地理北向的夹角；
-  反方位角：台站到震中的连线与地理北向的夹角；

一张图可以说明一切:
 [caption id="" align="alignnone" width="693"]\ |image0|
图1：震中距、方位角(az)、反方位角(baz)示意图.[/caption]

数学推导
~~~~~~~~

公式的推导需要简单的球面三角函数的知识。具体的推导可以参考Robert B.
Herrmann的作业题，网址如下：
 `http://www.eas.slu.edu/People/RBHerrmann/Courses/EASA462/`_
 作业题中的Ass06、Ass07、Ass08给出了计算震中距和方位角的原理。

相关代码
~~~~~~~~

广为流传的一个程序是distaz。在GMT、SAC等的源码里都可以找到。distaz代码很短，简单易懂，其采用的地球模型为椭球模型，精度上可以满足需求。

下面的链接给出了distaz的各种版本，包括C、Fortran、Java、Python以及CGI版本：
 `http://www.seis.sc.edu/software/distaz/`_

备注
~~~~

#. distaz的输入为sta\_lat sta\_lon evt\_lat evt\_lon，输出为 Delta Baz
   Az。注意顺序。
#. `CPS330`_\ 源码的VOLI/src/udelaz.c中利用了更高精度的地球模型，因而计算结果更精确，有兴趣的可以研究一下。

.. _`http://www.eas.slu.edu/People/RBHerrmann/Courses/EASA462/`: http://www.eas.slu.edu/People/RBHerrmann/Courses/EASA462/
.. _`http://www.seis.sc.edu/software/distaz/`: http://www.seis.sc.edu/software/distaz/
.. _CPS330: http://www.eas.slu.edu/eqc/eqccps.html

.. |image0| image:: http://i1313.photobucket.com/albums/t550/SeisManInfo/distaz_zps49aee6a8.jpg
