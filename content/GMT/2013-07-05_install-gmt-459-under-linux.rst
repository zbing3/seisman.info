GMT4.5.9在Linux下的安装
#######################

:date: 2013-07-05 12:46
:author: SeisMan
:modified: 2014-03-02
:category: GMT
:tags: 编译, GMT4
:slug: install-gmt-459-under-linux

.. contents::

说明
====

::

    本文适用于GMT 4.5.7至4.5.9版本，由于这三个版本已经过时，因而本文不再更新。

GMT从4.5.7开始，原来的几个源码包现在合并成了一个，安装起来相对要更简单一些。GMT 4.5.9于2013年1月1日正式发布，这个版本依然主要只是bug修订，但是安装过程中还是有一些细节的变化。

下载
====

官方网站：\ `http://gmt.soest.hawaii.edu/`_

日本镜像：\ `ftp://ftp.scc.u-tokai.ac.jp/pub/gmt`_

需要下载的源码包包括：

- `gmt-4.5.9.tar.bz2`_
- `gshhg-gmt-nc3-2.2.3.tar.bz2`_
- `netcdf-3.6.3.tar.gz`_

安装
====

安装netcdf
----------

.. code-block:: bash

    $ tar -zxvf netcdf-3.6.3.tar.gz # 解压netcdf
    $ cd netcdf-3.6.3 # 进入netcdf文件夹
    $ ./configure --prefix=/usr/local/netcdf-3.6.3 # configure, prefix指定netcdf的安装路径
    $ make # 编译netcdf
    $ sudo make install # 安装netcdf
    $ cd .. # 退回到netcdf上级目录[/code]

安装GMT
-------

.. code-block:: bash

    $ tar -jxvf gmt-4.5.9.tar.bz2 # 解压GMT
    $ cd GMT4.5.9 # 进入GMT文件夹
    $ ./configure --prefix=/usr/local/GMT-4.5.9 --enable-netcdf=/usr/local/netcdf-3.6.3/
         # 配置GMT。prefix为GMT安装路径，--enable-netcdf为前面netcdf的安装路径
    $ make gmt # 编译GMT自己的可执行文件及库文件
    $ make suppl # 编译其他人提供的GMT扩展包及库文件
    $ sudo make install-gmt # 安装GMT自己的可执行文件
    $ sudo make install-suppl # 安装GMT扩展包
    $ sudo make install-data # 安装GMT数据，其实就是拷贝share目录
    $ sudo make install-man # 拷贝man到share
    $ sudo make install-doc # 拷贝doc到share
    $ cd .. # 返回GMT上级目录

安装海岸线数据
--------------

.. code-block:: bash

    $ tar -jxvf gshhg-gmt-nc3-2.2.3.tar.bz2 # 解压GMT需要的海岸线数据
    $ sudo cp -r gshhg-gmt-nc3-2.2.3 /usr/local/GMT-4.5.9/share/coast
         # 拷贝数据，将所有文件拷贝到share下的coast目录中

修改环境变量
------------

在.bashrc中加入如下语句：

.. code-block:: bash

    export GMTHOME=/usr/local/GMT-4.5.9
    export PATH=${GMTHOME}/bin:$PATH

备注
====

- GMT 4.5.9有两个类似的包：gmt-4.5.9.tar.bz2和gmt-4.5.9-non-gpl.tar.bz2。两个包的主要区别在于triangulate命令的代码是否遵循GPL协议。
- GSHHG数据包含两个版本：gshhg-gmt-nc3-2.2.3.tar.bz2和gshhg-gmt-nc4-2.2.3.tar.bz2，其分别对应netcdf-3.x.x和netcdf-4.x.x。因而数据包要根据NetCDF的版本进行选择。
- netcdf-3.x.x的最终版本为3.6.3，netcdf-4.x.x的最新版本是4.3.0。
- 按需选择版本，注意netcdf与GSHHG的对应关系。

依赖包
======

编译过程中可能出现一些错误，主要是相关的依赖包没有安装，因而可能需要安装如下软件包：

.. code-block:: bash
    
    sudo yum install g++ libXt-devel libXaw-devel libXmu-devel libSM-devel


.. _`http://gmt.soest.hawaii.edu/`: http://gmt.soest.hawaii.edu/
.. _`ftp://ftp.scc.u-tokai.ac.jp/pub/gmt`: ftp://ftp.scc.u-tokai.ac.jp/pub/gmt
.. _gmt-4.5.9.tar.bz2: ftp://ftp.scc.u-tokai.ac.jp/pub/gmt/gmt-4.5.9.tar.bz2
.. _gshhg-gmt-nc3-2.2.3.tar.bz2: ftp://ftp.scc.u-tokai.ac.jp/pub/gmt/gshhg-gmt-nc3-2.2.3.tar.bz2
.. _netcdf-3.6.3.tar.gz: http://www.unidata.:wucar.edu/downloads/netcdf/ftp/netcdf-3.6.3.tar.gz
