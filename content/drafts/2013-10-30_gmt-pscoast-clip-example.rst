GMT进阶之pscoast的clip功能的例子
#####################################################
:date: 2013-10-30 00:15
:author: SeisMan
:category: GMT
:tags: GMT脚本
:slug: gmt-pscoast-clip-example

问题描述
~~~~~~~~

已有etopo数据，其包含了全球地形以及海水深度数据，现绘制全球地图，要求有全球海岸线和地形数据。

代码1
~~~~~

[code lang="bash"]
 #!/bin/bash
 R=0/360/-60/60
 J=M24c

grdraster 8 -R$R -I2m -Gout.grd
 makecpt -Cglobe -T-11500/8500/2000 -Z > colors.cpt
 grdimage out.grd -J$J -R$R -Ccolors.cpt -K > a.ps
 pscoast -J$J -R$R -B60/30 -W1/0.5p -N1 -O >> a.ps
 [/code]
 效果如下：

|image0|

这里可以很明显地看出，海岸线与地形是不重合的。一开始以为是脚本的问题，想想才明白，地形与海岸线不匹配是正常的，其差异是由于大陆架造成的。理论上可以通过修改cpt文件，使得大于0和小于0的地形的颜色对比更强烈一些。不过这不是这篇博文所关注的东西。

代码2
~~~~~

[code lang="bash"]
 #!/bin/bash
 R=0/360/-60/60
 J=M24c

grdraster 1 -R$R -I5m -Gout.grd
 makecpt -Cglobe -T-11500/8500/2000 -Z > colors.cpt

pscoast -J$J -R$R -Gc -K -V > a.ps
 grdimage out.grd -J$J -R$R -Ccolors.cpt -K -O -V >> a.ps
 pscoast -J$J -R$R -Q -K -O -V >> a.ps
 pscoast -J$J -R$R -B60/30 -W1/0.5p -N1 -O -V >> a.ps
 [/code]
 |image1|

这里使用了三个pscoast命令，第一个pscoast将陆地区域clip出来，第二个pscoast关闭clip，第三个pscoast绘制海岸线。效果还不错。

代码3
~~~~~

[code lang="bash"]
 #!/bin/bash
 R=0/360/-60/60
 J=M24c

grdraster 1 -R$R -I5m -Gout.grd
 makecpt -Cglobe -T-11500/8500/2000 -Z > colors.cpt

pscoast -J$J -R$R -Sc -K -V > a.ps
 grdimage out.grd -J$J -R$R -Ccolors.cpt -K -O -V >> a.ps
 pscoast -J$J -R$R -Q -K -O -V >> a.ps
 pscoast -J$J -R$R -B60/30 -W1/0.5p -N1 -O -V >> a.ps
 [/code]

.. figure:: http://ww3.sinaimg.cn/large/c27c15bejw1e9yzbk9hvoj21kw0ol109.jpg
   :align: center
   :alt: 

与代码2类似，这里只绘制出了海洋部分的地形。

.. |image0| image:: http://ww1.sinaimg.cn/large/c27c15bejw1e9yzd1xfowj21kw0oljyq.jpg
.. |image1| image:: http://ww1.sinaimg.cn/large/c27c15bejw1e9yzdzdopxj21kw0oln23.jpg
