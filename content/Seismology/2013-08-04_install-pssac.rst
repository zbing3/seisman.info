pssac之安装
###########

:date: 2013-08-04 15:13
:author: SeisMan
:category: 地震学软件
:tags: pssac, 编译
:slug: install-pssac

.. contents::

pssac是Prof. Lupei Zhu根据GMT的psxy命令改写的一个小程序，利用GMT强大的绘图功能来绘制SAC文件。

下载
====

.. code-block:: bash

 $ mkdir pssac
 $ cd pssac
 $ wget http://www.eas.slu.edu/People/LZhu/downloads/pssac.tar
 #下载基于GMT4.0的pssac包
 $ wget http://www.eas.slu.edu/People/LZhu/downloads/pssac.c
 #下载基于GMT4.5的pssac源码
 $ tar xvf pssac.tar
 $ cp pssac.c pssac #用新的pssac.c替换旧的
 $ cd pssac

修改Makefile
============

用你最喜欢的编辑器打开Makefile文件，在文件头部加上1-5行的内容，并根据自己的情况稍作修改：

.. code-block:: bash

 NETCDFHOME=/usr/local/netcdf
 GMTHOME=/usr/local/GMT

 GMT_INC=-I${GMTHOME}/include -I${NETCDFHOME}/include
 GMT_LIBS=-L${GMTHOME}/lib -lgmt -lpsl -lgmtps -L${NETCDFHOME}/lib -lnetcdf -lm -s -Wl,-rpath,${NETCDFHOME}/lib

 CFLAGS = -O ${GMT_INC}

 pssac: pssac.o sacio.o
    $(LINK.c) -o $@ $@.o sacio.o $(GMT_LIBS)

 clean:
    rm -f pssac *.o

-  NETCDFHOME为你安装的netcdf的路径，需要根据自己的情况修改
-  GMTHOME为你安装的GMT的路径，需要根据自己的情况修改
-  GMT_INC指定了GMT和netcdf的头文件位置
-  GMT_LIBS指定了编译过程中的库文件
-  -L指定了在编译过程中要在哪些路径寻找库文件
-  -lgmt -lpsl -lgmtps为GMT/lib下的几个库文件
-  -lnetcdf是netcdf的库文件
-  -lm代表链接数学函数库
-  -s代表删除可执行文件符号表和重定位信息。（这个牵涉到的知识有点多，有兴趣的也许可以看\ `这本书`_\ ）
-  -Wl,-rpath,${NETCDFHOME}/lib指定了程序运行时候搜索动态库的路径，注意与-L的区别这个解释起来有点复杂，放在文章的最后再解释一下吧。

编译
====

.. code-block:: bash

 $ make
 cc -O -I/usr/local/local/GMT/include -I/usr/local/local/netcdf/include -c -o pssac.o pssac.c
 cc -O -I/usr/local/local/GMT/include -I/usr/local/local/netcdf/include -c -o sacio.o sacio.c
 cc -O -I/usr/local/local/GMT/include -I/usr/local/local/netcdf-3.6.3/include -o pssac pssac.o sacio.o -L/usr/local/local/GMT/lib -lgmt -lpsl -lgmtps -L/usr/local/local/netcdf-3.6.3/lib -lnetcdf -lm -s -Wl,-rpath,/usr/local/local/netcdf-3.6.3/lib

编译过程就是简单的make，如果没有错误的话应该会出现下面三行。

执行
====

直接./pssac应该就会出来关于pssac的使用说明，如果报其他错，可以向我反馈。

关于-W的说明
======================================

在netcdf下可能会有这么几个库文件：

::

     libnetcdf.a  libnetcdf.la  libnetcdf.so  libnetcdf.so.4  libnetcdf.so.4.0.0 

当然也有可能只有下面这个几个文件

::

     libnetcdf.a libnetcdf_c++.a libnetcdf_c++.la libnetcdf.la 

出现这个差异的原因不详，可能是由于netcdf的版本不同造成的。简单解释一下其中的区别，.a文件为静态库文件，.so文件为动态库文件，.la文件大概是.a文件的说明文件，可以直接用vi打开查看，由于不是真正的库文件，所以这里忽略。

编译的过程很复杂，网上也很多文章可以看，我也不是这方面的专家，就不乱说了。编译的最后需要进行链接生成可执行文件。链接库文件可以分为静态链接和动态链接两种。静态链接把需要的库文件打包在生成的可执行文件中，这样无论以后链接的库文件是删除了还是改名了，都不会影响这个可执行文件的执行。而动态链接只是将这个动态库文件的位置记录在了可执行文件中，当这个可执行文件被执行时，首先要载入这个动态库文件。

动态链接与静态链接相比，动态链接要求库文件不可随意修改，灵活性不够，但显然动态链接得到的可执行文件要更小一些。

gcc编译器在使用-l选项链接库文件时，优先链接动态库文件。（当然没有动态库文件的时候只能链接静态库文件了。）可以通过-static选项强制gcc链接静态库文件，但是这样也会导致很多系统级别的库文件被迫使用静态链接（比如libc.a），这可能会导致你的可执行文件非常大。所以-static这样的方式是不太好的。

回到netcdf，如果你的netcdf是第一种情况，既有.a又有.so，那么编译的时候会链接.so文件，在执行的时候也要知道.so文件的位置，这就需要-Wl,-rpath,${NETCDFHOME}/lib了。如果你的netcdf下只有.a文件，那么链接的时候就只是静态链接，就不会存在这样的问题，-Wl,-rpath,${NETCDFHOME}/lib选项也就不需要了。

如果没看懂的话，就加上这个选项，反正不会错。

对旧版本的说明
==============

在编译旧版本的pssac的时候，可能会出现类似“BOOLEAN类型未定义”这样的错误，这是因为在C99标准之前是没有bool类型的定义，C99标准中增加了_Bool类型作为布尔类型，而BOOLEAN应该是用户自己定义的。具体可以参考下面两个维基条目：

`http://zh.wikipedia.org/wiki/%E5%B8%83%E7%88%BE\_%28%E6%95%B8%E6%93%9A%E9%A1%9E%E5%9E%8B%29#C`_

`http://zh.wikipedia.org/wiki/C%E8%AF%AD%E8%A8%80#C99`_

可以通过在pssac.c重定义数据类型来修正整个错误。在pssac.c代码的前部加上如下两个typedef语句中的任何一个都可以：

.. code-block:: C

 typedef _Bool BOOLEAN;
 typedef GMT_LONG BOOLEAN;

其中GMT_LONG是Prof. Zhu 的新pssac.c代码中的用法。

备注
====

经常接触程序的人，还是应该多了解一些编译链接的知识的。推荐一篇静态链接和动态链接的文章\ `点击查看`_

修订历史
========

- 2013-04-17：初稿；
- 2013-04-19：加入了对旧版本pssac.c的讨论。

.. _这本书: http://book.douban.com/subject/3652388/
.. _`http://zh.wikipedia.org/wiki/%E5%B8%83%E7%88%BE\_%28%E6%95%B8%E6%93%9A%E9%A1%9E%E5%9E%8B%29#C`: http://zh.wikipedia.org/wiki/%E5%B8%83%E7%88%BE_%28%E6%95%B8%E6%93%9A%E9%A1%9E%E5%9E%8B%29#C
.. _`http://zh.wikipedia.org/wiki/C%E8%AF%AD%E8%A8%80#C99`: http://zh.wikipedia.org/wiki/C%E8%AF%AD%E8%A8%80#C99
.. _点击查看: http://blog.csdn.net/gengshenghong/article/details/7105165
