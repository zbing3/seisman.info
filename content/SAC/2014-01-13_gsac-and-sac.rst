GSAC指出的SAC存在的一些问题
############################

:date: 2014-01-13 01:22
:author: SeisMan
:category: SAC
:tags: 函数库
:slug: gsac-and-sac

个人理解，GSAC是SAC的重新实现。GSAC在文档的开头指出了SAC的一些问题：

-  闭源：曾经的SAC是Fortran语言写的，且不公开源代码，后期改为C语言，遗留了很多问题，导致代码难以阅读，目前源代码依然不可以自由分发；
-  图形窗口X11已经过时：X11精度不高，绘图效果较差；
-  SAC头段中未定义二进制类型：SAC软件可以正确处理little endian和big endian的问题，但是SAC格式本身并不包含任何关于endian，因而数据格式不能自解释。
-  PZ的问题：仪器响应文件中一个很关心的问题是仪器的输入和输出分别是什么，这个在RESP文件中说的很清楚，但是SAC PZ文件中却没有相关信息；
-  GMT和matlab：越来越多的人使用matlab处理sac数据，使用GMT绘制波形，官方应该提供权威的版本。
-  函数库接口：libsac.a和libsacio.a是SAC提供的两个函数库，使用起来较麻烦，对用户不够友好；
