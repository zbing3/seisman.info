GMT网格数据之ETOPO1
###################

:date: 2013-08-11 15:53
:author: SeisMan
:category: GMT
:tags: 地形, 数据, 网格
:slug: etopo1-of-gmt-grid
:summary: 全球地形ETOPO1。

.. contents::

ETOPO1包含了全球地形和海洋深度，采样间隔为1弧分，是目前精度最高的global relief数据。

官方主页位于：\ `http://www.ngdc.noaa.gov/mgg/global/`_

其分为两个版本，Ice Surface和Bedrock，两个版本基本一致。不同之处在于在处理南极洲和Greenland地形时，前者给出的是加上冰盖层之后的高程，后者给出的是岩床的高程。

对于每个版本又细分为grid-registered和cell-registered，其中grid-registered是权威版本，cell-registered是衍生版本，因而\ **推荐下载使用grid-registered版本**\ 。

在每个子版本下又有多种数据格式， netCDF，binary， xyz，tiff。

我选择的是\ **grid-registered版本**\ 的\ **binary格式**\ 。

下载
====

::

    http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO1/data/ice_surface/grid_registered/binary/etopo1_ice_g_i2.zip

解压
====

::

    7za e etopo1_ice_g_i2.zip

解压之后的.bin文件为二进制网格文件，.hdr文件为头段文件

拷贝
====

::

    sudo cp etopo1_ice_g_i2.bin /usr/local/GMT-4.5.9/share/dbase

修改grdraster.info
==================

直接将下面的语句复制到grdraster.info中即可。关于语句为什么要这么写，需要参考hdr文件的内容。

::

    9 "ETOPO1 Ice Surface"          "m"     -R-180/180/-90/90       -I1m            GG i 1          0       -32768  etopo1_ice_g_i2.bin     L

同理，对于bedrock版本的网格数据，其grdraster.info为

::

    10 "ETOPO1 Bedrock"             "m"     -R-180/180/-90/90       -I1m            GG i 1          0       -32768  etopo1_bed_g_i2.bin     L

备注
====

如果下载的是netCDF格式的网格文件，需要利用如下命令将数据转换为binary格式：

::

    grdreformat ETOPO1_Ice_g_gmt4.grd etopo1_ice_g_i2.bin=bs -N -V

.. _`http://www.ngdc.noaa.gov/mgg/global/`: http://www.ngdc.noaa.gov/mgg/global/
