GMT(4.5.6前版本)在Linux下的安装
#####################################################
:date: 2013-07-04 12:13
:author: SeisMan
:category: GMT
:tags: 安装, 编译
:slug: install-old-gmt-under-linux

下载
~~~~

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
~~~~

[code lang="bash"]
 [seisman@info ]$ cd GMTinstall
 [seisman@info ]$ ls
 GMT4.5.6\_doc.tar.bz2 GMT4.5.6\_share.tar.bz2 GMT4.5.6\_src.tar.bz2
 GMT4.5.6\_suppl.tar.bz2 GMT4.5.6\_triangle.tar.bz2
 GSHHS2.1.1\_coast.tar.bz2 GSHHS2.1.1\_full.tar.bz2
GSHHS2.1.1\_high.tar.bz2
 [seisman@info ]$ tar xvfz netcdf-3.6.3.tar.gz
 [seisman@info ]$ for i in \*.bz2;do tar jxvf $i;done
 [/code]

这时候生成如下文件夹：

::

    netcdf-3.6.3 GMT4.5.6 share

安装
~~~~

NetCDF安装
^^^^^^^^^^

[code lang="bash"]
 [seisman@info ]$ cd netcdf-3.6.3
 [seisman@info ]$ ./configure --prefix=/usr/local/netcdf-3.6.3
 [seisman@info ]$ make
 [seisman@info ]$ sudo make install
 [seisman@info ]$ cd ..
 [/code]

-  prefix参数表示想装到/usr/local/netcdf-3.6.3
-  make编译生成可执行文件
-  make
   install将编译后的可执行文件、头文件以及库文件安装到prefix指定的路径
-  make
   install需要root权限，有些发行版可以sudo，有些发行版需要su切换到root

GMT安装
^^^^^^^

[code lang="bash"]
 [seisman@info ]$ cd GMT4.5.6
 [seisman@info ]$ ./configure --prefix=/usr/local/GMT
--enable-netcdf=/usr/local/netcdf-3.6.3
 [seisman@info ]$ make
 [seisman@info ]$ sudo make install
 [seisman@info ]$ cd ..
 [/code]

-  prefix指定GMT安装路径，--enable-netcdf后加netcdf的安装路径

复制相关数据文件
^^^^^^^^^^^^^^^^

[code lang="bash"]
 [seisman@info ]$ sudo cp -r GMT4.5.6/share/ /usr/local/GMT/
 [seisman@info ]$ sudo cp -r share/coast /usr/local/GMT/share
 [/code]

环境变量
~~~~~~~~

在.bashrc中加入如下语句
 [code]
 export GMTHOME=/usr/local/GMT
 export PATH=/usr/local/GMT/bin:$PATH
 [/code]

一些错误
~~~~~~~~

netcdf编译错误
^^^^^^^^^^^^^^

netcdf编译过程中可能出现的错误：

::

    gcc: error trying to exec 'cc1plus': execvp: 没有那个文件或目录
    make[2]: *** [netcdf.lo] 错误 1

原因：未安装g++
 解决办法：

::

    sudo apt-get install g++

GMT编译错误
^^^^^^^^^^^

可能出现的错误：

::

    make[2]: 正在进入目录 `/home/s2214/GMT/GMT4.5.6/src/xgrid'
    gcc -O2 -Wall -fPIC -fno-strict-aliasing -I/home/s2214/GMT/GMT4.5.6/src -I/usr/local/netcdf/include -c -o xgrid_Panner.o xgrid_Panner.c
    xgrid_Panner.c:4:31: error: X11/Xaw/Scrollbar.h: 没有那个文件或目录

可以看出大概的意思是X11下缺少了一些东西，所以导致xgrid无法编译通过。

xgrid实际上是一个grid文件的有界面编辑器，用处应该不是很大，大多数系统中在configure的时候是找不到X11的库和头文件的，所以
xgrid不会编译，但是在装了部分X11的软件包（但是没有装完全）的情况下，configure的时候可以找到X11库和头文件，但是由于缺少关键程序包，所以无法编译通过。

可以通过在对GMT进行configure的时候关闭xgrid的编译选项，即configure命令改为：

::

    ./configure --prefix=/usr/local/GMT --enable-netcdf=/usr/local/netcdf --disable-xgrid

.. _`http://gmt.soest.hawaii.edu/`: http://gmt.soest.hawaii.edu/
.. _镜像: ftp://ftp.scc.u-tokai.ac.jp/pub/gmt/
.. _`http://www.unidata.ucar.edu/downloads/netcdf/ftp/netcdf-3.6.3.tar.gz`: http://www.unidata.ucar.edu/downloads/netcdf/ftp/netcdf-3.6.3.tar.gz
