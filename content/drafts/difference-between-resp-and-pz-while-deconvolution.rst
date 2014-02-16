用RESP和PZ去除仪器响应的差别
#####################################################
:date: 2013-06-29 00:18
:author: SeisMan
:category: 基础知识
:tags: 仪器响应
:slug: difference-between-resp-and-pz-while-deconvolution

前面介绍了RESP文件和PZ文件，下面分别用两种响应文件进行去仪器响应，比较二者的区别。
 下载地址：\ `SAC数据`_  `RESP文件`_  `PZ文件`_

RESP去除仪器响应
~~~~~~~~~~~~~~~~

[code]
 [seisman@info ]$ sac
 SEISMIC ANALYSIS CODE [02/01/2012 (Version 101.5c)]
 Copyright 1995 Regents of the University of California

SAC> r ./2013.144.05.40.09.0195.IU.COLA.00.BHZ.M.SAC
 SAC> rmean; rtr; taper
 SAC> trans from evalresp fname ./RESP.IU.COLA.00.BHZ to none freq 0.01
0.05 5 7
 Using response from user-specified file: (./RESP.IU.COLA.00.BHZ).
 Extracting evresp response for COLA, BHZ...
 Station (COLA ), Channel (BHZ )
 SAC> w RESP.SAC
 SAC> q
 [/code]

PZ去除仪器响应
~~~~~~~~~~~~~~

[code]
 [seisman@info]$ sac
 SEISMIC ANALYSIS CODE [02/01/2012 (Version 101.5c)]
 Copyright 1995 Regents of the University of California

SAC> r ./2013.144.05.40.09.0195.IU.COLA.00.BHZ.M.SAC
 SAC> rmean; rtr; taper
 SAC> trans from polezero subtype
./SAC\_PZs\_IU\_COLA\_BHZ\_00\_2012.258.04.00.00.0000\_2599.365.23.59.59.99999
to none freq 0.01 0.05 5 7
 Using polezero response for COLA, BHZ, IU, 00...
 Station (COLA ), Channel (BHZ )
 SAC> w PZ.SAC
 SAC> q
 [/code]

结果对比
~~~~~~~~

-  对比生成的两个SAC文件，波形很类似。RESP.SAC的最值在10的6次方量级，PZ.SAC的最值在10的-3次方量级，这是单位的问题。首先SAC的默认的位移单位为nm。RESP文件中有指定仪器的输入单位为m/s，这行虽然以#开头，其在去仪器响应的时候是可以被SAC读取的，因而利用RESP去仪器响应时SAC知道输入的单位是什么，SAC自然也会进行单位的转换。而PZ文件中虽然给出了输入单位为m，但PZ文件中以#开头的行是被忽略的，所以SAC其实并不知道仪器的输入单位是什么，直接去仪器响应，得到的波形单位为m，而SAC在不知道单位的情况下“自做聪明”直接将其单位改写成了nm，这就导致了波形量级上的错误。因而\ **SAC在利用PZ文件去仪器响应的时候要乘以10的9次方进行单位转换**\ 。
-  对单位进行校正后，对二者做互相关，发现互相关的结果峰值位于0处，这意味着二者不存在时间延迟的问题。PZ文件中没有任何时间延迟的概念，而RESP中在滤波过程中存在时间延迟，并给出了延迟估计和延迟校正。互相关峰值在0处意味着在用RESP做反卷积的时候对数字滤波器做了反卷积，并且对时间问题做了校正。
-  两个波形的差在10的2次方量级，大概占信号的千分之一，这个误差也许是因为PZ文件没有将全部阶段考虑进去导致的，不过这个影响很小。

备注
~~~~

-  SAC的PZ文件中所有以星号开头的行都是注释，基本不起到任何作用。在大量数据批处理的过程中，可以直接用这些PZ文件去仪器响应，也可以先用脚本重新新建一个没有注释行的PZ文件，再去仪器响应。经过非严谨测试，在上千个数据的时候，后者速度可以提升几十倍。

修订历史
~~~~~~~~

-  2013-06-29：初稿；
-  2013-07-06：修改了“结果对比”中第一点的说明；

.. _SAC数据: http://pan.baidu.com/share/link?shareid=3171267740&uk=19892171
.. _RESP文件: http://pan.baidu.com/share/link?shareid=2175477867&uk=19892171
.. _PZ文件: http://pan.baidu.com/share/link?shareid=3164978357&uk=19892171
