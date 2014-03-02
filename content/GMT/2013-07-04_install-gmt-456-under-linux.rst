GMT4.5.6及更早版本在Linux下的安装
##################################

:date: 2013-07-04 12:13
:modified: 2014-03-02
:author: SeisMan
:category: GMT
:tags: 编译,GMT4
:slug: install-gmt-456-under-linux

.. contents::

说明
====

GMT 4.5.6以及之前的版本已过时很久，本文不再维护更新。

下载
====

GMT主页是\ `http://gmt.soest.hawaii.edu/`_\ ，在mirror下选择日本的一个\ `镜像`_\ ，下载如下软件包

::

    GMT4.5.6_doc.tar.bz2        #GMT文档，例子，手册
    GMT4.5.6_share.tar.bz2      #GMT运行时需要读取的一些重要文件
    GMT4.5.6_src.tar.bz2        #GMT主要源代码包
    GMT4.5.6_suppl.tar.bz2      #GMT补充包，包含了他人维护的一些GMT命令
    GMT4.5.6_triangle.tar.bz2   #GMT三角剖分代码，这个是Non GPL的，所以GMT源码中包含的是另一个三角剖分代码
    GSHHS2.1.1_coast.tar.bz2    #海岸线、边界、湖泊数据。包含了中等、低、粗三种精度
    GSHHS2.1.1_full.tar.bz2     #海岸线、边界、湖泊数据。最高精度
    GSHHS2.1.1_high.tar.bz2     #海岸线、边界、湖泊数据。高精度

GMT源码的编译依赖于另一个软件包NetCDF。NetCDF是GMT网格数据的主要格式。

下载地址：\ `http://www.unidata.ucar.edu/downloads/netcdf/ftp/netcdf-3.6.3.tar.gz`_

把这些软件包放在同一个文件夹中，下面假定这个文件夹叫做GMTinstall，以便于说明安装过程。

解压
====

.. code-block:: bash

 [seisman@info ]$ cd GMTinstall
 [seisman@info ]$ ls
 GMT4.5.6_doc.tar.bz2 GMT4.5.6_share.tar.bz2 GMT4.5.6_src.tar.bz2
 GMT4.5.6_suppl.tar.bz2 GMT4.5.6_triangle.tar.bz2
 GSHHS2.1.1_coast.tar.bz2 GSHHS2.1.1_full.tar.bz2 GSHHS2.1.1_high.tar.bz2
 [seisman@info ]$ tar xvfz netcdf-3.6.3.tar.gz
 [seisman@info ]$ for i in \*.bz2;do tar jxvf $i;done

这时候生成如下文件夹：

::

    netcdf-3.6.3 GMT4.5.6 share

安装
====

NetCDF安装
----------

.. code-block:: bash

 [seisman@info ]$ cd netcdf-3.6.3
 [seisman@info ]$ ./configure --prefix=/usr/local/netcdf-3.6.3
 [seisman@info ]$ make
 [seisman@info ]$ sudo make install
 [seisman@info ]$ cd ..

- prefix参数表示想装到/usr/local/netcdf-3.6.3
- make编译生成可执行文件
- make install将编译后的可执行文件、头文件以及库文件安装到prefix指定的路径
- make install需要root权限，有些发行版可以sudo，有些发行版需要su切换到root

GMT安装
-------

.. code-block:: bash

 [seisman@info ]$ cd GMT4.5.6
 [seisman@info ]$ ./configure --prefix=/usr/local/GMT --enable-netcdf=/usr/local/netcdf-3.6.3
 [seisman@info ]$ make
 [seisman@info ]$ sudo make install
 [seisman@info ]$ cd ..

- prefix指定GMT安装路径;
- --enable-netcdf后加netcdf的安装路径

复制相关数据文件
----------------

.. code-block:: bash

 [seisman@info ]$ sudo cp -r GMT4.5.6/share/ /usr/local/GMT/
 [seisman@info ]$ sudo cp -r share/coast /usr/local/GMT/share

环境变量
========

在.bashrc中加入如下语句

.. code-block:: bash

 export GMTHOME=/usr/local/GMT
 export PATH=/usr/local/GMT/bin:$PATH

依赖包
======

编译过程中可能出现一些错误，主要是相关的依赖包没有安装，因而可能需要安装如下软件包：

::
    
    sudo yum install g++ libXt-devel libXaw-devel libXmu-devel libSM-devel

.. _`http://gmt.soest.hawaii.edu/`: http://gmt.soest.hawaii.edu/
.. _镜像: ftp://ftp.scc.u-tokai.ac.jp/pub/gmt/
.. _`http://www.unidata.ucar.edu/downloads/netcdf/ftp/netcdf-3.6.3.tar.gz`: http://www.unidata.ucar.edu/downloads/netcdf/ftp/netcdf-3.6.3.tar.gz
