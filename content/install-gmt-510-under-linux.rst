GMT5.1.0在Linux下的安装
#####################################################
:date: 2013-11-06 00:53
:author: SeisMan
:category: GMT5
:tags: 安装
:slug: install-gmt-510-under-linux

GMT5的第一个正式版5.1.0于2013年11月05日正式发布了。GMT5相对于GMT4的变化还是相当大的（幸好提供了兼容模式），对于用惯了GMT4的人来说，估计一时半会没法适应GMT5。不管怎样，先把GMT5安装上再说。

下载
~~~~

GMT 5.1.0 需要下载三个文件：

#. GMT源码：\ `http://gmtrac.soest.hawaii.edu/files/download?name=gmt-5.1.0-src.tar.gz`_
#. 全球海岸线数据GSHHG：\ `ftp://ftp.soest.hawaii.edu/gshhg/gshhg-gmt-nc4-2.2.4.tar.gz`_
#. 全球数字图表DCW：\ `ftp://ftp.soest.hawaii.edu/dcw/dcw-gmt-1.1.0.tar.gz`_

喜欢使用svn的，也可以利用下面的命令获取GMT源码：
 [code]svn checkout svn://gmtserver.soest.hawaii.edu/gmt5/trunk
gmt-dev[/code]

解决依赖关系
~~~~~~~~~~~~

GMT的编译和运行，依赖其他一些软件，看ps文件需要ghostscript，编译需要cmake(>=2.8.5)，网格文件需要netCDF(>=4.0,需要支持netCDF-4/HDF5)。其他可有可无的依赖包括Perl兼容正则表达式库\ `PCRE`_\ ，地理空间数据抽象库\ `GDAL`_\ ，以及Fourier变换库\ `FFTW`_
。如果想要自行编译文档的话还需要\ `Sphinx`_\ 。

这些依赖文件，如果想要完全自行编译，可配置的选项太多，曾经看过一天的文档没有配置出结果。所以还是直接利用各个Linux发行版的软件包管理器直接安装比较好。

Ubuntu/Debian
^^^^^^^^^^^^^

很久没用Ubuntu了，aptitude应该与apt-get是类似的东西。下面的命令安装了gs、编译基本软件、cmake、netcdf和、gdal。如果想要安装其他依赖，请自行搜索。
 [code]sudo aptitude install ghostscript build-essential cmake
libnetcdf-dev libgdal1-dev[/code]

RHEL, CentOS, Fedora
^^^^^^^^^^^^^^^^^^^^

这三者都是采用yum作为包管理器，其官方源中不包含安装GMT所需要的软件。因而，使用这些Linux发行版的用户，一定要自行添加\ `EPEL`_\ 源。关于如何添加EPEL源的方法，可以参考以前博客中的\ `这篇`_\ 文章。

下面的命令安装了GMT需要的三个软件cmake、netcdf和gdal：
 [code]sudo yum install cmake28 netcdf-devel gdal-devel[/code]
 如果想要安装其他依赖，命令如下（没找到sphinx）：
 [code]sudo yum install pcre-devel fftw-devel [/code]

安装GMT
~~~~~~~

解决了依赖关系之后，就可以安装了。
 [code lang="bash"]
 $ ls
 dcw-gmt-1.1.0.tar.gz gmt-5.1.0-src.tar.gz gshhg-gmt-nc4-2.2.4.tar.gz
 $ tar -zxvf gmt-5.1.0-src.tar.gz
 $ tar -zxvf dcw-gmt-1.1.0.tar.gz
 $ tar -zxvf gshhg-gmt-nc4-2.2.4.tar.gz
 $ ls
 dcw-gmt-1.1.0 dcw-gmt-1.1.0.tar.gz gmt-5.1.0 gmt-5.1.0-src.tar.gz
 gshhg-gmt-nc4-2.2.4 gshhg-gmt-nc4-2.2.4.tar.gz
 $ cd gmt-5.1.0
 $ cp cmake/ConfigUserTemplate.cmake cmake/ConfigUser.cmake
 $ vi cmake/ConfigUser.cmake # 修改Config文件
 [/code]

修改ConfigUser.cmake以满足用户自定义的需求，将需要修改的行最前面的“#”去掉，并根据实际情况修改，一个基本的示例如下：

::

    set (CMAKE_INSTALL_PREFIX "/opt/GMT-5.1.0")
    set (GSHHG_ROOT "/export/home/seisman/backup/seisware/GMT/5.1.0/gshhg-gmt-nc4-2.2.4")
    set (COPY_GSHHG TRUE)
    set (DCW_ROOT "/export/home/seisman/backup/seisware/GMT/5.1.0/dcw-gmt-1.1.0")
    set (COPY_DCW TRUE)
    set (FLOCK TRUE)

CMAKE\_INSTALL\_PREFIX设置GMT的安装路径；

GSHHG\_ROOT为GSHHG数据的位置，需要对下载下来的压缩文件进行解压，并给定绝对路径；COPY\_GSHHG为TRUE会将GSHHG数据复制到GMT/share/coast下；

DCW\_ROOT设置DCW数据的位置，需给定绝对路径，COPY\_DCW将数据复制到GMT/share/dcw下；
 FLOCK设置开启文件锁定功能。

修改完毕后，进行编译：
 [code]
 $ mkdir build
 $ cd build/
 $ cmake ..
 [/code]
 ``cmake ..``\ 会检查GMT对软件的依赖关系，我的检查结果如下：

::

    *  Options:
    *  Found GSHHG database       : /export/home/seisman/backup/seisware/GMT/5.1.0/gshhg-gmt-nc4-2.2.4 (2.2.4)
    *  Found DCW-GMT database     : /export/home/seisman/backup/seisware/GMT/5.1.0/dcw-gmt-1.1.0
    *  NetCDF library             : /usr/lib64/libnetcdf.so
    *  NetCDF include dir         : /usr/include
    *  GDAL library               : /usr/lib64/libgdal.so
    *  GDAL include dir           : /usr/include/gdal
    *  FFTW library               : /usr/lib64/libfftw3f.so
    *  FFTW include dir           : /usr/include
    *  Accelerate Framework       : 
    *  Regex support              : PCRE (/usr/lib64/libpcre.so)
    *  File locking               : TRUE
    *  License restriction        : no
    *  Triangulation method       : Shewchuk
    *  Build mode                 : shared
    *  Build GMT core             : always [libgmt.so]
    *  Build PSL library          : always [libpsl.so]
    *  Build GMT supplements      : yes [supplements.so]
    *  Build proto supplements    : none
    *
    *  Locations:
    *  Installing GMT in          : /opt/GMT-5.1.0
    *  GMT_DATADIR                : /opt/GMT-5.1.0/share
    *  GMT_DOCDIR                 : /opt/GMT-5.1.0/share/doc
    *  GMT_MANDIR                 : /opt/GMT-5.1.0/share/man
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /export/home/seisman/backup/seisware/GMT/5.1.0/gmt-5.1.0/build

检查完毕，开始编译：
 [code]
 $ make
 $ sudo make install
 [/code]

自行编译文档
~~~~~~~~~~~~

如果系统中安装了sphinx和LaTeX，则可以自行编译文档。（其实直接用官方已经编译好的文档即可）
 [code]
 $ make docs\_man
 $ make docs\_html
 $ make docs\_pdf
 $ sudo make install
 [/code]

修改环境变量
~~~~~~~~~~~~

在.bashrc中加入如下语句：
 [code lang="bash"]
 export GMTHOME=/opt/GMT-5.1.0
 export PATH=${GMTHOME}/bin:$PATH
 [/code]

参考来源
~~~~~~~~

1.\ `http://gmtrac.soest.hawaii.edu/projects/gmt/wiki/BuildingGMT`_
 2.\ `GMT4.5.9在Linux下的安装`_

.. _`http://gmtrac.soest.hawaii.edu/files/download?name=gmt-5.1.0-src.tar.gz`: http://gmtrac.soest.hawaii.edu/files/download?name=gmt-5.1.0-src.tar.gz
.. _`ftp://ftp.soest.hawaii.edu/gshhg/gshhg-gmt-nc4-2.2.4.tar.gz`: ftp://ftp.soest.hawaii.edu/gshhg/gshhg-gmt-nc4-2.2.4.tar.gz
.. _`ftp://ftp.soest.hawaii.edu/dcw/dcw-gmt-1.1.0.tar.gz`: ftp://ftp.soest.hawaii.edu/dcw/dcw-gmt-1.1.0.tar.gz
.. _PCRE: http://www.pcre.org/
.. _GDAL: http://www.gdal.org/
.. _FFTW: http://www.fftw.org/
.. _Sphinx: http://sphinx-doc.org/
.. _EPEL: http://fedoraproject.org/wiki/EPEL
.. _这篇: http://seisman.blog.ustc.edu.cn/index.php/archives/476
.. _`http://gmtrac.soest.hawaii.edu/projects/gmt/wiki/BuildingGMT`: http://gmtrac.soest.hawaii.edu/projects/gmt/wiki/BuildingGMT
.. _GMT4.5.9在Linux下的安装: http://seisman.info/install-new-gmt-under-linux.html
