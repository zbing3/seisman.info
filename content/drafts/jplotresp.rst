JPlotResp：绘制地震仪器响应
#####################################################
:date: 2013-07-19 14:13
:author: SeisMan
:category: 地震学软件
:tags: Java, 仪器响应
:slug: jplotresp

前言
~~~~

要理解仪器响应，就要看RESP的格式，更重要是直观地看仪器响应的振幅相位谱。

前面介绍的Resp文件和SAC
PZ文件都只是给出了一堆零极点以及放大系数等各种参数。JPlotResp是用来绘制地震仪器响应的软件，可以帮助直观地看到任意台站的仪器响应。

主页：\ `http://www.isti2.com/JPlotResp/`_

简介
~~~~

-  Java语言
-  底层由JEvalResp计算仪器响应
-  JEvalResp是evalresp的Java版本

功能
~~~~

-  支持在线查询，指定台网、台站以及时间即可；
-  直接绘制本地Resp文件；
-  支持多种仪器响应：速度、加速度、位移；
-  绘制振幅相位谱、复数谱；
-  指数坐标或者线性坐标；

截图
~~~~

启动界面：

比较实用的是读取本地文件，然后Plot。

.. figure:: http://ww1.sinaimg.cn/large/c27c15bejw1e6s2t1rctyj20vf0la41w.jpg
   :align: center
   :alt: 

读取本地Resp文件：

.. figure:: http://ww2.sinaimg.cn/large/c27c15bejw1e6s2zsr6mdj20sz0m1wi2.jpg
   :align: center
   :alt: 

绘制的振幅响应谱：

Display可以选择显示仪器响应的哪些部分以获得更清晰或者更多的信息，还可以将图直接保存为高质量的jpg文件。

.. figure:: http://ww2.sinaimg.cn/large/c27c15bejw1e6s3g07nyfj20s00kmwid.jpg
   :align: center
   :alt: 

.. _`http://www.isti2.com/JPlotResp/`: http://www.isti2.com/JPlotResp/
