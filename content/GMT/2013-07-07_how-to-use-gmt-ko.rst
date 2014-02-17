GMT使用-K和-O的技巧
###################

:date: 2013-07-07 11:30
:author: SeisMan
:category: GMT
:tags: GMT技巧,GMT脚本,GMT选项
:slug: how-to-use-gmt-ko
:summary:

.. contents::

-K和-O是GMT的17个标准选项中最常用但最容易出错的两个。

用法回顾
========

- 如果一张图只需要一个命令就可以画出来，则不需要-K和-O选项；
- 如果一张图由两个命令绘制出来，第一个命令需要使用-K，第二个命令需要使用-O；
- 如果一张图由多个命令组成，第一个命令使用-K，中间命令使用-K和-O，最后一个命令使用-O；
- 第一个命令使用重定向符号">"创建新文件并写入PS命令；
- 余下所有命令绘图命令使用重定向符号">>"向PS文件中追加新的PS命令；

经典错误
========

- 已经写好的一个绘图脚本，想要在往图里加点东西。在脚本的最后加了个命令，使用了-O，但是却忘了把原来最后一个命令的-O改成-K -O。这样最后一个命令应该没有效果，或者gs直接报错。
- 第一个命令绘制海岸线，第二个命令绘制地形，导致地形把海岸线覆盖了，想要交换两个命令的顺序，结果忘记将第一个命令的-K改成-O，忘记将第二个命令的-O改成-K。这样应该完全没结果吧。
- 想要在第一个命令前再加一个绘图命令，也记得把原来第一个命令的-K改成-K -O，但是忘记把">"改成">>"。

新手常犯的错误太多，一时想不起了。

完全避免犯错的技巧
==================

下面的技巧可以几乎完全避免使用-K、-O以及重定向符号过程中可能出现的错误（前提是要理解这个简单的技巧为什么可以帮助你避免犯错）。我自己用Perl写脚本，有些人用Bash写脚本，所以这里给出Perl和Bash两个版本。

Bash版
------

.. code-block:: bash

 #!/bin/bash
 #
 # GMT template
 #
 PS=example.ps
 J=X6i
 R=0/1/0/1

 # Begin GMT Plot
 psxy -J$J -R$R -T -K > $PS

 # now begin your real plot commands
 # every command should be with "-K" "-O" and ">>"

 # End GMT Plot
 psxy -J$J -R$R -T -O >> $PS

 # Plot finished. Now you can convert PS to other format
 #

Perl版
------

.. code-block:: perl
 #!/usr/bin/perl -w
 #
 # GMT template
 #

 use strict;
 my $J="X6i";
 my $R="0/1/0/1";
 my $PS="template.ps";

 # Begin GMT Plot
 &GMT_open($J, $R, $PS);

 # now begin your real plot commands
 # every command should be with "-K" "-O" and ">>"

 # End GMT Plot
 &GMT_close($J, $R, $PS);

 # Plot finished. Now you can convert PS to other format
 #

 # subroutine definition
 sub GMT_open {
 my ($J, $R, $PS ) = @_;
    system("psxy -J$J -R$R -T -K > $PS");
 }

 sub GMT_close {
 my ($J, $R, $PS ) = @_;
    system("psxy -J$J -R$R -T -O >> $PS");
 }

一点点解释
----------

-T选项忽略所有输入，即输入为空，相当于/dev/null。因而这两个psxy命令实际上不会对生成的图形产生任何影响。第一个psxy命令产生了头段信息，最后的psxy命令生成了尾巴，中间的命令（零个、一个或者多个）不需要头段也不需要尾巴，因而中间的所有命令需要-K、-O选项，并使用重定向">>"。这样不管以后怎么修改整个脚本，在KO和重定向这里都不会出现问题。Perl版本中将这两个命令写成了GMT_open()和GMT_close()函数，整个脚本就可以作为所有GMT脚本的模板了。不太懂Bash，所以不会改写。

备注
====

- 印象中这个技巧在官方文档的脚本中出现过，但是没有将其作为一种技巧来说，所以貌似未得到推广；
- 每个GMT命令默认都会输出头段和尾巴，这样的设计合理吗？为什么不是绘图命令完全抛弃头段和尾巴，由两个单独的命令向PS文件中写头段和尾巴？这样的设计也许不太符合GMT命令的整体风格；
- 究竟有没有效果？用过之后才有评价的资格。
- 曾经我也用bash写脚本，学会Perl之后就彻底抛弃了bash。bash的功能过于简单，只能做简单的判断和循环，文本处理的功能大都依赖于其他外部命令，比如gawk、sed、cut、sort，这意味着你除了要学习bash的语法，还要学习gawk等等各种工具，简单的几页搞定，难一点的又是一本书。Perl的优点很多，跨平台；语言风格和C非常像，易学；很多内置命令速度很快；强大的模块支持，直接调用模块实现并行、ftp管理、网页浏览；变量是字符串，同时也可以是数字。使用Perl，没有做不到的，只有想不到的。抛弃Bash，投奔Perl吧。（PS：据说Python、Ruby也是非常优秀的脚本语言。）

修订历史
========

- 2013-07-07：初稿；
- 2013-08-24：修订了bash脚本中的一个笔误；
- 2013-11-06：修订脚本，使用-T选项，不再使用\ ``/dev/null``
