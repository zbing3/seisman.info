pssac绘图之reduce velocity对齐
#####################################################
:date: 2013-08-07 00:18
:author: SeisMan
:category: GMT, SAC, 地震学软件
:tags: pssac
:slug: reduce-velocity-alignment-with-pssac

不晓得Reduce Velocity翻译成中文该怎么翻，Peter Shearer的Introduction to
Seismology 中的一张图很好的解释了reduce velocity的概念：
 [caption width="997" align="alignnone"]\ |image0| 图1[/caption]

左图是标准的时距曲线X-T（也有人称走时图），左图的效果不甚理想，几条曲线斜率相近，密密麻麻放在一起看不清，由此得到了右图Reduced的时距曲线X-（T-X/8），其中8就是这里的reduce
velocity，在这种图下，走时曲线更容易看了。

还是利用上一篇中生成的那些地震数据做实验。

先看看一个正常的不做任何时间对齐的剖面图（其实按照文件起始时间对齐了）：
 [code]./pssac -JX5i -R0/1420/10/40 -B200/5 -Edt-5 -M0.5/-1 \*.z >
a.ps[/code]
 [caption width="769" align="alignnone"]\ |image1| 图2[/caption]
 再来看看reduce velocity的效果：
 [code]./pssac -JX5i -R0/1420/10/40 -B200/5 -Ed12 -M0.5/-1 \*.z >
a.ps[/code]
 [caption width="784" align="alignnone"]\ |image2| 图3[/caption]
 这里reduce取了12，然后就大概把初至波给对齐了。reduce
velocity的实质是将所有trace的起始时间都减去
“X/V”，其中X是震中距，V是reduce 速度。

.. |image0| image:: http://ww3.sinaimg.cn/large/c27c15bejw1e79u16qvocj20rp0eqgmg.jpg
.. |image1| image:: http://ww4.sinaimg.cn/large/c27c15bejw1e79u29s0uqj20ld0ld761.jpg
.. |image2| image:: http://ww1.sinaimg.cn/large/c27c15bejw1e79u3s0076j20ls0kv75y.jpg
