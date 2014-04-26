GMT技巧之地理坐标与笛卡尔坐标混合体
###################################

:author: SeisMan
:date: 2014-04-26 09:00
:category: GMT4
:tags: GMT技巧
:slug: mix-geographical-coordinate-with-cartesian-coordinate

提出问题
========

要绘制这么一张图，X轴是经度（地理坐标），Y轴是深度（笛卡尔坐标），如下图：

.. figure:: http://ww4.sinaimg.cn/large/c27c15bejw1efspvlx6egj21kw171766.jpg
   :alt: mix-geographical-coordinate-with-cartesian-coordinate
   :width: 700px

分析问题
========

#. 因为Y轴是线性坐标，所以必然只能选择线性投影，即\ ``-JX``\
#. 线性投影的情况下，图的主体很简单，关键在于X轴坐标的“度”符号上
#. 为了是X有一个“度”符号，就必须使得命令知道X轴为地理坐标，GMT的B选项提供了这样一个功能，可以使用\ ``-Bg40/50/0/40``\ ，这里的\ ``g``\ 告诉命令即便使用\ ``-JX``\ 投影，也认为其是地理坐标。由于是地理坐标，“度”符号就很容易出来了。
#. 使用\ ``-Bg40/50/0/40``\ 存在两个问题

   #. 虽然是线性投影，但是由于使用了地理坐标，GMT会默认将底图类型设置为fancy。这一点可以通过\ ``gmtset BASEMAP_TYPE plain``\ 来搞定。
   #. 此种写法导致X轴和Y轴均被当作地理坐标，所以Y轴也有一个“度”符号。

#. 尝试过把X轴和Y轴都当作线性坐标，然后对于X轴设置其单位为特殊的“度”符号，此法看似可行，实际上GMT设置了单位与标注之间的距离，通过单位设置的“度”符号明显离标注的距离较远，不太美观。

解决问题
========

下面利用了B选项的一个特性来解决这个问题：

.. code-block:: bash

   #/bin/bash
   R=40/50/0/40
   J=X20c/15c
   PS=map.ps
   gmtset BASEMAP_TYPE plain    # 设置底图类型为plain型

   psxy -R$R -J$J -T -K > $PS   # 写入PS文件头

   psbasemap -Rg$R -J$J -B2/5SN -K -O >> $PS    # 绘制X轴
   psbasemap -R$R -J$J -B2/5EW -K -O >> $PS     # 绘制Y轴

   # 这里放置其它绘图命令，不再使用B选项

   psxy -R$R -J$J -T -O >> $PS  # 写入PS文件尾

在《\ `GMT进阶之被滥用的-B选项 <{filename}/GMT/2013-08-23_abused-b-option.rst>`_\ 》一文中有提到，B选项的作用实际上就是绘制边框。若脚本中所有命令都使用了相同的B选项，实际上会多次绘制边框，只是每一次绘制都会完全覆盖前一次的边框，所以用户看不出来区别。因而在很多情况下，只需要在一个命令中使用B选项即可。

这里使用了两个psbasemap命令，其中第一个psbasemap只绘制两个X轴，注意\ ``-Rg$R``\ 中的\ ``g``\ ，第二个psbasemap只绘制两个Y轴，这样边框就设计好了，接下来要做的就只是保证其它命令都不使用B选项即可。
