GMT4更新至4.5.11
#####################################################
:date: 2013-11-07 00:17
:author: SeisMan
:category: GMT
:tags: 安装
:slug: gmt-4511-release

2013年11月5日，GMT4由4.5.9更新至4.5.10。这个新版本只是修订了一些bug，同时全球海岸线数据GSHHG也由2.2.3更新至2.2.4。

不过由于GMT4.5.10的安装脚本存在bug，稍后又发布了GMT4.5.11。

GMT 4.5.11的安装方法与GMT
4.5.9基本相同，因而可以参考以前的博文《\ `GMT4.5.9在Linux下的安装`_\ 》。

《\ `GMT4.5.9在Linux下的安装`_\ 》中介绍了如何编译netCDF3以及GMT4.5.9。目前GMT开始逐渐使用netCDF
4，逐渐不再支持netCDF 3了。因而官方的建议是：使用netCDF
4，且不需要自行编译，直接使用Linux各发行版的软件包管理器安装netCDF
4（一个主要的原因是手动编译netCDF4要比手动编译netCDF3复杂的多）。

对于Ubuntu/Debian：
 [code lang="bash"]sudo aptitude install libnetcdf-dev
libgdal1-dev[/code]

对于RHEL/CentOS/Fedora，需要先加入\ `EPEL`_\ 源，再安装netcdf：
 [code lang="bash"]sudo yum install netcdf-devel gdal-devel[/code]

然后编译GMT，
 [code]
 $ ./configure --prefix=/usr/local/GMT-4.5.11 # 不需要--enable-netcdf了
 $ make gmt
 $ make suppl
 $ sudo make install-gmt
 $ sudo make install-suppl
 $ sudo make install-data
 $ sudo make install-man
 $ sudo make install-doc
 [/code]
 其他类似。

最后，提醒一句，GSHHG数据一定要与netcdf版本配套才可以！

同时，GMT5的第一个正式版本5.1.0也出来啦。

.. _GMT4.5.9在Linux下的安装: http://seisman.info/install-new-gmt-under-linux.html
.. _EPEL: http://fedoraproject.org/wiki/EPEL
