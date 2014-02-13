pssac绘图之单个地震图
#####################################################
:date: 2013-08-05 00:00
:author: SeisMan
:category: GMT, SAC, 地震学软件
:tags: pssac
:slug: plot-single-trace-with-pssac

pssac中从GMT继承的选项都很简单，不再多说。pssac自己的选项中，上一篇博文中介绍了-I、-Q、-r这三个简单的选项，本文将通过一系列例子去理解pssac的其他几个选项在绘制单个地震图时会有什么样的效果。

首先找个顺手的地震图试试，SAC自带的样本地震就是个不错的选择：
 [code]
 SAC> fg seis
 SAC> lh b e depmax depmin

FILE: SEISMOGR - 1
 --------------
 b = 9.459999e+00
 e = 1.945000e+01
 depmax = 1.520640e+00
 depmin = -1.569280e+00
 SAC> w seis
 [/code]
 这个数据的横坐标范围大概是(9.4,19.5)，纵坐标范围大概(-1.6,1.6)。

使用如下命令即可得到下图：
 [code]./pssac -JX6i/3i -R9/20/-2/2 seis > a.ps [/code]
 [caption width="672" align="alignnone"]\ |image0| 图1[/caption]

这个命令是使用pssac需要的最简单的命令了，画出来的图和想象中的一样。为了更清楚地看到其他选项对于地震图的影响，先给这张图加个边框。
 [code]./pssac -JX6i/3i -R9/20/-2/2 -B1/0.4 seis > a.ps [/code]
 [caption width="805" align="alignnone"]\ |image1| 图2[/caption]
 为了更效果明显一些，所以横纵坐标都选的偏大了一点。

下面利用pssac自带的选项来进一步修改这个图：
 [code]./pssac -JX6i/3i -R9/20/-2/2 -B1/0.4 -C11/16 -G0/255/0/0 -Wblue
seis > a.ps [/code]
 [caption width="784" align="alignnone"]\ |image2| 图3[/caption]
 -C
选项指定要绘制的区域，-C11/16代表只绘制11s到16s之间的数据，这个相当于实现了SAC中的cut命令，随便一个地震数据，需要哪段画哪段。
-G0/255/0/0表示将所有振幅>0的区域都涂上绿色，这个在剖面图中用的会比较多一点。-Wblue指定线条颜色为蓝色（其实这是GMT的
选项，只是在pssac源程序中当作一般选项来处理了）。

[code]./pssac -JX6i/3i -R9/20/-2/2 -B1/0.4 -S3 seis > a.ps[/code]
 [caption width="770" align="alignnone"]\ |image3| 图4[/caption]

-S选项给出的是trace的shift量，由上图可以看出，trace整体向右平移了3s。（为什么要设计这个选项？我不太清楚。）这里引入了-S和-C的优先级问题。即先是数据平移再截取数据，还是先截取数据再进行平移。

下面的例子可以给出答案：
 [code]./pssac -JX6i/3i -R9/20/-2/2 -B1/0.4 -C11/16 -S3 seis > a.ps
[/code]
 [caption width="780" align="alignnone"]\ |image4| 图5[/caption]

与前面两张图对比一下可以看出来，数据首先整体平移了3s，即当前的数据x范围为（12，21），而-C指定的范围为（11，16），所以实际画出的区域是（12，16）。所以-S的优先级要大于-C。（可以得出结论-S是用来修改文件起始时间的吗？）

下面看一下-V选项（为了图看起来方便，这里-J、-R、-B都改了）：
 [code]./pssac -JX3i/6i -R-2/2/9//20 -B0.4/1 seis -V > a.ps [/code]
 [caption width="433" align="alignnone"]\ |image5| 图6[/caption]

由这个例子可以看出-V的功能跟GMT中的-P可不一样，-V导致的结果是横轴变成了振幅，纵轴变成了时间。一个可能的用途上，某些具体情况下，地震图中的某个震相到时可能与某个界面的深度成正比，通过垂直绘制地震图并将多个地震图排在一起，并把纵坐标通过某个关系改成相应的深度，那么一张界面变化图就出来了。一个常见的例子是接收函数。

-E选项和-M选项一般在绘制单个地震图时不会使用，当然只要你理解了其中的细节，用了也不会出什么大事。
 [code]./pssac -JX6i/3i -R9/20/-2/2 -B1/0.4 seis -M1 > a.ps[/code]
 [caption width="773" align="alignnone"]\ |image6| 图7[/caption]
 可以很明显的看到振幅变小了。

下面的例子展示了-E单独使用时出现的问题：
 [code]./pssac -JX6i/3i -R9/20/-2/2 -B1/0.4 -Edt-5 seis > a.ps [/code]
 [caption width="784" align="alignnone"]\ |image7| 图8[/caption]

-E选项指定了要使用剖面。t代表按照某个时间对齐，-5代表文件起始时间，这意味着所有的文件都要按照文件起始时间对齐，即所有文件的b对应的时间为0。

下面修改R的范围来显示全部的地震图：
 [code]./pssac -JX6i/3i -R0/11/-2/2 -B1/0.4 -Edt-5 seis > a.ps [/code]
 [caption width="791" align="alignnone"]\ |image8| 图9[/caption]

这下地震图都显示出来了，另一个问题在于，剖面类型在这里究竟起到了怎么的效果？事实是没有效果。剖面类型d指定了y轴为震中距，那么这个地震图应该在y=3.4附近。而实际上地震图在0附近。

下面的例子解决了单个地震图的剖面类型无效的问题，这里y轴的范围取为(3,4):
 [code]./pssac -JX6i/3i -R0/11/3/4 -B1/0.4 -Edt-5 seis -M1 > a.ps[/code]
 [caption width="754" align="alignnone"]\ |image9| 图10[/caption]

这里地震图的位置对了，是一个最简单的剖面图了，如前所说，剖面图实际上丢弃了地震图的绝对振幅信息，你可以试试通过-M选项修改其振幅，不过，剖面图的相对信息还是在的，这些应该会在下一篇博文中说。

至此，如何利用pssac绘制单个地震图就说完啦。

.. |image0| image:: http://ww4.sinaimg.cn/large/c27c15bejw1e79t4bhh5kj20io07z3yp.jpg
.. |image1| image:: http://ww4.sinaimg.cn/large/c27c15bejw1e79t6m0k1jj20md0c3755.jpg
.. |image2| image:: http://ww2.sinaimg.cn/large/c27c15bejw1e79t9zyouyj20ls0bjaaw.jpg
.. |image3| image:: http://ww2.sinaimg.cn/large/c27c15bejw1e79tcwmqqgj20le0bddgp.jpg
.. |image4| image:: http://ww4.sinaimg.cn/large/c27c15bejw1e79te42hg8j20lo0bm750.jpg
.. |image5| image:: http://ww4.sinaimg.cn/large/c27c15bejw1e79tf8vh70j20c10kjgmg.jpg
.. |image6| image:: http://ww2.sinaimg.cn/large/c27c15bejw1e79tgd3th5j20lh0bk3z7.jpg
.. |image7| image:: http://ww2.sinaimg.cn/large/c27c15bejw1e79thduts7j20ls0bqjrw.jpg
.. |image8| image:: http://ww4.sinaimg.cn/large/c27c15bejw1e79ticii9aj20lz0bujs7.jpg
.. |image9| image:: http://ww2.sinaimg.cn/large/c27c15bejw1e79tj8ve04j20ky0budg9.jpg
