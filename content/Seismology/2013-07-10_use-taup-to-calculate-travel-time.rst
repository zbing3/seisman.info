走时计算软件TauP
################

:date: 2013-07-10 00:53
:author: SeisMan
:category: 地震学软件
:tags: 走时, TauP
:slug: use-taup-to-calculate-travel-time

.. contents::

简介
====

TauP由\ `University of South Carolina`_\ 开发，是一个用于计算走时以及射线路径、反射点、穿透点等的一个软件包。其可以在多个平台上运行，支持多种地球速度模型以及自定义模型，支持多种震相。

安装
====

- 下载最新版本：\ `http://www.seis.sc.edu/taup/index.html`_
- TauP要求平台安装有Java1.6以上版本，可以在终端输入java -version检查自己是否已安装或版本是否正确。
- 解压下载的TauP软件包，将文件夹移至/usr/local或其他目录下
- 在.bashrc中设置环境变量：
    
.. code-block:: bash

   export TAUP_HOME=/usr/local/TauP-2.0
   export PATH=${TAUP_HOME}/bin:$PATH

- \ ``source .bashrc``\ 使其生效

命令简介
========

#. TauP和ttimes一样都是基于Buland和Chapman于1983年提出的方法的taup_time和ttimes具有相同的功能，都是计算震相理论到时，不同之处在于taup可以利用自己定义的速度模型，且taup包含了一个震相语法分析器（phase parser），因而可以研究更多不常见的震相。
#. taup_pierce用于计算射线在各个速度分界面的穿透点，即射线经过了多少角度以及多长时间才到达某一深度。其中比较有意思的两个选项是-az和-baz，当给出事件经纬度、震中距和方位角az时，就可以输出各个穿透点的经纬度位置而不仅仅只是角度而已，这样就可以画出很多paper上常见的反射点位置什么的。-baz类似~另外-rev、-turn和-under允许自由选择感兴趣的反射点，-pierce则更强大，使得你可以知道任意深度的穿透位置。有一点不足之处在于不同的选项会导致输出的内容差别很大，但是输出却没有给出每列的含义。
#. taup_path用于绘制射线路径，其生成一个包含两列数据的文件，第一列是离开震源的角度，第二列是射线所在深度（实际上半径长度），这样一个xy文件可以用于后续的绘图。另外，-gmt选项会将生成一个包含xy数据的GMT脚本，执行该脚本就可以绘制一个不错的射线路径图，可是这个脚本看起来很简单，但是实际是经过精心设计的，因此修改起来会有点麻烦。
#. taup是整个程序的GUI界面，常用的功能都有，只是不是很完善。用它来看看震相大概的到时以及路径还是很方便的。
#. taup_curve用于绘制走时曲线，其也可以生成一个GMT脚本，这个脚本的修改比较简单些，两个选项-reddeg、-redkm不知是干嘛的
#. taup_setsac用于将震相到时、射线参数等信息写入头段中。（要是早知道taup可以干这个就好了）按作者的说法，这个命令还是有一堆不完善的地方的，个人感觉不是主要问题。

备注
====

- 详细信息看TauP的manual

.. _University of South Carolina: http://sc.edu/
.. _`http://www.seis.sc.edu/taup/index.html`: http://www.seis.sc.edu/taup/index.html
