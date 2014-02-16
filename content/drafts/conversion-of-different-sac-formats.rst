SAC不同格式间的转换
#####################################################
:date: 2013-08-04 01:11
:author: SeisMan
:category: SAC
:tags: 格式转换
:slug: conversion-of-different-sac-formats

SAC文件格式包括二进制格式和ASCII格式，平常接触的都是二进制格式的，毕竟二进制格式相对于ASCII格式有很多优点，比如读写速度更快、文件大小更小。下面讨论SAC的两种格式以及另外一种常见的数据格式(自变量+因变量两列数据)之间的转换。

1、二进制格式转ASCII格式

::

    SAC> r sacfile
    SAC> w alpha sacfile.ascii

有时数据遇到问题的时候，可以转换成ASCII格式，看看里面的内容。

2、ASCII文件转二进制格式

::

    SAC> r alpha sacfile.ascii
    SAC> w sacfile

3、时间序列（因变量）转SAC二进制格式

::

    SAC> readtable data1
    SAC> w sacfile

4、时间序列（自变量+因变量）文件转SAC二进制文件

::

    SAC> readalpha content xy data2
    SAC> w sacfile

非时间序列数据（任意的xy数据）都可以用SAC来处理以实现相应的功能，这也就是SAC自称其为“一个用于处理连续信号尤其是时间序列数据的通用交互式程序”的原因。

5、SAC二进制文件转时间序列（因变量或自变量+因变量）

没法用命令直接做到，比较合适的做法是写一个C或FORTRAN调用读取SAC文件，然后以数组形式写入文件。
