GMT进阶之修改箭头形状
#####################################################
:date: 2013-11-11 00:04
:author: SeisMan
:category: GMT
:tags: GMT技巧, GMT脚本
:slug: gmt-vector-shape

感觉GMT默认的箭头很丑，一直以为GMT没法修改箭头的形状，细细看了gmtdefaults才发现，箭头其实也是可以自定义的。

在GMT4中，可以通过修改默认参数VECTOR\_SHAPE来自定义箭头形状。其取值范围为[-2,2]，默认值为0。

在GMT5中，这个参数改名为MAP\_VECTOR\_SHAPE。

如下图所示：

.. figure:: http://ww2.sinaimg.cn/large/c27c15bejw1ea5rsreu85j20mo0rgab6.jpg
   :align: center
   :alt: 

坐标的坐标对应了不同的VECTOR\_SHAPE的取值，默认值为0，此时的箭头是个等腰三角形。个人感觉VECTOR\_SHAPE取[0.5,1]的值看上去比较美观。

下面为绘图所用脚本：
 [code lang="bash"]
 #!/bin/bash
 # GMT 4
 R=0.8/3/-2.5/2.5
 J=X6c/8c
 B=0.5/0.5W
 PS=vector.ps

psxy -R$R -J$J -T -K > $PS

for i in -2 -1.5 -1 -0.5 0 0.5 1 1.5 2;
 do
 gmtset VECTOR\_SHAPE $i
 psxy -R$R -J$J -B$B -Sv -Gblack -K -O <<EOF >> $PS
 1 $i 0 5
 EOF
 done;

psxy -R$R -J$J -T -O >> $PS

rm .gmt\*
 [/code]
