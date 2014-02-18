SAC 101.6的一个bug及其解决办法
##############################

:date: 2013-08-18 00:22
:author: SeisMan
:category: SAC
:tags: Bug
:slug: solution-to-a-bug-of-sac-101-6

SAC 101.6相对于前一版本改动过大，所以引入了不少新的bug。

一个bug是在读入一个或若干个SAC文件后，使用sort命令对内存中的文件进行排序，经过sort后的文件的台站位置信息丢失。

目前还不清楚产生这个bug的原因是什么，解决办法为设置环境变量SAC\_USE\_DATABASE值为0，即

::

    export SAC_USE_DATABASE=0

