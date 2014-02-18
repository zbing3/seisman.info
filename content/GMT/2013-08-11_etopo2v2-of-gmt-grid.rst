GMT网格数据之ETOPO2v2
######################

:date: 2013-08-11 15:50
:author: SeisMan
:category: GMT
:tags: 地形, 数据, 网格
:slug: etopo2v2-of-gmt-grid
:summary: 全球地形数据etopo2。

ETOPO2v2与ETOPO5类似，也是高程+海底地形数据，其采样间隔为2弧分。

官方地址：\ `http://www.ngdc.noaa.gov/mgg/global/etopo2.html`_

官方提供了提供了很多版本，\ **ETOPO2v2c**\ 和\ **ETOPO2v2g**\ 分别代表两种不同的网格表示方式，详情参见GMT。其中\ **ETOPO2v2c**\ 是权威版本，建议选择ETOPO2v2c。

**ETOPO2v2c**\ 下又有许多格式可以选择，如下所示

::

 ETOPO2v2c
  ├── GRD98：ETOPO2v2c_i2_LSB_GRD98.zip
  ├── HDF：ETOPO2v2c_HDF.zip
  ├── netCDF：ETOPO2v2c_f4_netCDF.zip
  └── raw_binary：ETOPO2v2c_f4_LSB.zip和ETOPO2v2c_i2_LSB.zip

其中netCDF，grd98和raw binary为GMT所支持。由于grdraster只支持raw binary网格，对于netCDF和grd98格式的网格首先要转换为raw binary格式才能用，所以下面使用raw binary格式网格数据。

1.下载Little-endian，16位整型的二进制网格文件(GMT的grdraster不支持float型的网格数据)

::

    wget -c http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO2/ETOPO2v2-2006/ETOPO2v2c/raw_binary/ETOPO2v2c_i2_LSB.zip

2.解压

::

    7za e ETOPO2v2c_i2_LSB.zip

解压之后的.bin文件为二进制网格文件，.hdr文件为头段文件

3.拷贝

::

    sudo cp ETOPO2v2c_i2_LSB.bin /usr/local/GMT-4.5.9/share/dbase

4.修改grdraster.info（一些细节需要参考hdr文件）

::

    8 "ETOPO2 global topography"    "m"     -R-180/180/-90/90       -I2m            PG i 1          0       -32768  ETOPO2v2c_i2_LSB.bin    L

5.画图测试

.. code-block:: bash

 #!/bin/bash
 verbose=-V

 grdraster 8 -Rg -I2m -Gout.grd $verbose
 makecpt -Cglobe -T-10500/8000/1000 -Z $verbose > colors.cpt
 grdimage out.grd -Ba60g30 -Rg -Yc -Xc -JN0/25c -Ccolors.cpt -K $verbose > etopo5.ps
 psscale -Ba2500f500::/:"m": -Ccolors.cpt -D12.5c/-2c/15c/.35ch -O $verbose >> etopo5.ps

 rm out.grd colors.cpt

.. _`http://www.ngdc.noaa.gov/mgg/global/etopo2.html`: http://www.ngdc.noaa.gov/mgg/global/etopo2.html
