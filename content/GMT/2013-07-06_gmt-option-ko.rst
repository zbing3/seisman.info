GMT进阶之深入理解-K和-O选项
###########################

:date: 2013-07-06 00:39
:author: SeisMan
:category: GMT
:tags: GMT选项
:slug: gmt-option-ko

.. contents::

-K和-O是GMT的两个标准选项，其用法很简单，一张图和一段文字就可以明白一切。但是同时-K和-O选项却是日常GMT绘图中最常出错的地方，很多时候这样的错误很让人摸不着头脑。这里首先简单介绍-K和-O的选项，然后试着去探究一下-K和-O选项在代码中代表什么，在下一篇博文中给出使用-K和-O选项的一个技巧。

如GMT Technical Reference and Cookbook中第4.4.6节所说，任意一个完整的PS文件都必须包含头段（初始化），正文（绘图部分），尾巴（输出图像）。

.. figure:: http://ww2.sinaimg.cn/large/c27c15bejw1e8cjep63rej20sg0bidgo.jpg
   :width: 700 px
   :alt: 

GMT的每个绘图命令默认都会同时输出头段、正文以及尾巴。如左图所示，如果一张图只需要一个命令就可以画出来，那么就不需要-K和-O选项。如中图所示，如果一张图由两个命令绘制出来，第一个命令需要省略尾巴部分（使用-K），第二个命令需要省略头段部分（使用-O）。更常见的情况如右图所示，一张图由多个命令组成，第一个命令省略尾巴（-K），中间命令省略头段和尾巴（-K -O），最后一个命令省略头段（-O）。另外一个需要注意的地方是重定向符号，第一个命令使用">"，后面所有的命令使用">>"。

下面研究一下-K和-O的细节。

如下五条命令生成了五个ps文件：

.. code-block:: bash

 psxy -JX6i -R0/1/0/1 < /dev/null > a.ps
 psxy -JX6i -R0/1/0/1 -K < /dev/null > b.ps
 psxy -JX6i -R0/1/0/1 -O < /dev/null > c.ps
 psxy -JX6i -R0/1/0/1 -K -O < /dev/null > d.ps
 psxy -JX6i -R0/1/0/1 -Sc1i -K -O > e.ps <<EOF
 0.5 0.5
 EOF

虽然五个ps文件只有第一个是语法上完全对且可以查看的PS文件，但是从这几个文件可以看出一些KO的细节。PS文件是可以直接用vi打开的。

a.ps和b.ps的区别在于-K，即b.ps中没有尾巴，因而得到PS的尾巴内容为：

::

    %%PageTrailer

    -295.276 -295.276 T 4.16667 4.16667 scale -90 R -595 0 T 0 A
    showpage

    %%Trailer

    end
    %%EOF

showpage和end还是可以看懂的。

查看一下d.ps和e.ps的内容，-K，-O，没有头段没有尾巴，只有正文。d.ps的输入为/dev/null，e.ps的输入为一个点。二者内容如下

d.ps:

::

    PSL_font_encode 0 get 0 eq {ISOLatin1+_Encoding /Helvetica /Helvetica PSL_reencode PSL_font_encode 0 1 put} if
    0 setlinecap
    0 setlinejoin
    3.32551 setmiterlimit

    %% PostScript produced by:
    %%GMT: psxy -JX6i -R0/1/0/1 -K -O
    %%PROJ: xy 0.00000000 1.00000000 0.00000000 1.00000000 0.000 1.000 0.000 1.000 +xy +a=6378137.000 +b=6356752.314245
    1 W
    0 A
    0 A

e.ps:

::

    PSL_font_encode 0 get 0 eq {ISOLatin1+_Encoding /Helvetica /Helvetica PSL_reencode PSL_font_encode 0 1 put} if
    0 setlinecap
    0 setlinejoin
    3.32551 setmiterlimit

    %% PostScript produced by:
    %%GMT:  psxy -JX6i -R0/1/0/1 -Sc1i -K -O
    %%PROJ: xy 0.00000000 1.00000000 0.00000000 1.00000000 0.000 1.000 0.000 1.000 +xy +a=6378137.000 +b=6356752.314245
    clipsave
    0 0 M
    1800 0 D
    0 1800 D
    -1800 0 D
    eoclip N
    1 W
    0 A
    FQ
    O1
    150 900 900 SC
    cliprestore
    0 A

还是看不懂，整个正文部分说了编码方式、字体，可能还有格式，注释中给出了该段正文中的命令，下面就是具体的参数，由于d.ps中psxy实际上没有输入，1
W、0 A、0 A可能是具体的命令，这几行在e.ps中也出现了。

看看a.ps文件的头段部分，内容很多，重要且能看懂的东西如下：

-  BoundingBox以及HiResBoundingBox
-  创建时间
-  landscape还是portrait
-  总页码
-  ISOLatin1+支持的特殊符号
-  所有GMT可用的字体
-  页面设置

没什么可总结的，没心思看PS的语法。
