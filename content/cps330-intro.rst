CPS330 : Computer Programs in Seismology
#####################################################
:date: 2014-01-01 18:36
:author: SeisMan
:category: 地震学软件
:tags: 合成地震图, 地球模型, 接收函数, 震源机制解
:slug: cps330-intro

CPS全称Computer Programs in
Seismology，是圣路易斯大学地震中心开发并维护的一款地震学软件包，其主要关注地震波在地壳和上地幔介质中的传播和解释。

主页：\ `http://www.eas.slu.edu/eqc/eqccps.html`_
 最新版本：3.30
 更新日期：2013-11-08

软件包中包含了完整的\ `说明文档`_\ ，即使不使用该软件，文档中的一些内容还是有参考价值的。

软件包的源码可以在\ `这里`_\ 申请，第一次下载的时候可以申请一下，以后其实可以从\ `FTP`_\ 直接下载。

软件包还在不断\ `更新`_\ 中。官方给了不少\ `教程`_\ ，不仅仅教授如何使用软件，同时也介绍了很多地震学的基础知识，同时还有不少用户的问题以及开发者的\ `回答`_\ 。另外官方也会有一些不错的\ `Notes`_\ 值得一看。

软件包包含了如下代码：

1. 合成地震图代码（主要是平层介质）

-  广义射线法；
-  波数积分法；
-  模态叠加法；
-  渐进射线理论；

2. 地壳结构研究

-  面波频散；
-  远震P波接收函数；
-  面波频散和接收函数联合反演；

3. 区域地震及远震震源反演

-  震源深度；
-  震源机制解；
-  地震矩；

4. GSAC

GSAC可以认为是SAC的重新实现，作者给了一些需要重写SAC的理由。

5. CALPLOT

为了实现代码的易移植性，CPS自带了CALPLOT绘图包。

.. _`http://www.eas.slu.edu/eqc/eqccps.html`: http://www.eas.slu.edu/eqc/eqccps.html
.. _说明文档: http://www.eas.slu.edu/eqc/eqc_cps/CPS/CPS330.html
.. _这里: http://www.eas.slu.edu/eqc/eqc_cps/CPS/cpslisc.html
.. _FTP: ftp://ftp.eas.slu.edu/pub/rbh/PROGRAMS.330
.. _更新: http://www.eas.slu.edu/eqc/eqc_cps/cpsbug.html
.. _教程: http://www.eas.slu.edu/eqc/eqc_cps/TUTORIAL/
.. _回答: http://www.eas.slu.edu/eqc/eqc_cps/Questions/
.. _Notes: http://www.eas.slu.edu/eqc/eqc_cps/workshop.html
