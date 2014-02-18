中国行政区划数据下载
#####################################################
:date: 2013-11-23 00:35
:author: SeisMan
:category: GMT, GMT5
:tags: GMT脚本, 数据, 格式转换, 网站
:slug: china-administrative-areas-data

GADM数据库
~~~~~~~~~~

GADM，是一个全球行政区划数据库。包括了几乎全部国家和地区的国界、省界以及更小的行政区划。

主页：\ `http://www.gadm.org/`_
 下载：\ `http://www.gadm.org/country`_

数据格式包括：shapefile、ESRI geodatabase、RData、Google Earth kmz
format。

在GADM中，country的定义为“any entity with an ISO country code”。关于ISO
country code，可以参考维基百科相关\ `词条`_\ 。

因而想要下载完整的中国数据，实际上需要下载四个文件：China、Hong
Kong、Macao、Taiwan。

数据格式选择shapefile。

可以在\ `http://www.gadm.org/version2`_\ 下载全球的行政区划数据，但非常不推荐。一方面是数据量偏大，另一方面是全球区划数据保存到一个文件中，难以整理。不如麻烦一点，需要哪个国家下哪个国家。

ogr2ogr
~~~~~~~

GMT目前还不能识别shapefile格式的数据，因而就需要将shapefile格式转换为GMT可识别的格式。转换工具为ogr2ogr，这是GDAL自带的一个命令，因而如果正确安装了GMT5的话应该是很容易找到这个命令。

以中国数据为例：

解压数据
^^^^^^^^

[code]$ unzip CHN\_adm.zip -d CHN\_adm[/code]

解压后得到一堆文件，其中CHN\_adm0.shp、CHN\_adm1.shp、CHN\_adm2.shp、CHN\_adm3.shp为实际需要的shapefile数据，0、1、2、3为第零、一、二、三级行政区划，基本相当于国界、省界、市界、区界。（是这么个说法吧。。）

格式转换
^^^^^^^^

命令从网上找到的，CHN\_adm0为要生成的数据的文件名前缀，但是为什么要出现两次，表示很不解。
 [code]
 $ ogr2ogr -f GMT -nln CHN\_adm0 CHN\_adm0 CHN\_adm0.shp
 $ ogr2ogr -f GMT -nln CHN\_adm1 CHN\_adm1 CHN\_adm1.shp
 $ ogr2ogr -f GMT -nln CHN\_adm2 CHN\_adm2 CHN\_adm2.shp
 $ ogr2ogr -f GMT -nln CHN\_adm3 CHN\_adm3 CHN\_adm3.shp
 [/code]

对于Hong
Kong、Macao、Taiwan的数据做类似操作，最终生成了一堆以gmt结尾的文件。共计10个，如下：

::

    CHN_adm0.gmt  CHN_adm2.gmt  HKG_adm0.gmt  MAC_adm0.gmt  TWN_adm1.gmt
    CHN_adm1.gmt  CHN_adm3.gmt  HKG_adm1.gmt  TWN_adm0.gmt  TWN_adm2.gmt

绘图测试
~~~~~~~~

国界
^^^^

绘制国界需要全部0级数据。

注意：数据为多段数据，在GMT4中需要使用-m选项，而GMT5已经可以自动处理多段数据，所以不需要使用-m选项。
 [code lang="bash"]
 R=72/136/15/54
 J=M15c
 PS=china.ps

gmt psxy -J$J -R$R -T -K -U > $PS
 gmt psxy -R$R -J$J CHN\_adm0.gmt -K -O >> $PS
 gmt psxy -R$R -J$J HKG\_adm0.gmt -K -O >> $PS
 gmt psxy -R$R -J$J MAC\_adm0.gmt -K -O >> $PS
 gmt psxy -R$R -J$J TWN\_adm0.gmt -K -O >> $PS
 gmt psxy -R$R -J$J -T -O >> $PS
 [/code]
 代码运行过程中GMT会出现如下的警告(或错误？)

::

    psxy: Bad OGR/GMT: @D record has more items than declared by @N

猜测是ogr2ogr转换的问题。在我的系统环境该警告不影响绘图效果，但评论中@vv指出在他的系统环境下会导致图形无法绘制。

效果图（缺了南海的九段线数据）：

.. figure:: http://ww2.sinaimg.cn/large/c27c15bejw1eaqdi4f56ij21ik17f0v0.jpg
   :align: center
   :alt: 

省级行政区划
^^^^^^^^^^^^

与上面的代码几乎一样，1级数据中0级数据，所以直接绘制1级数据即可，Macao没有1级数据，直接用0级数据。
 [code lang="bash"]
 R=72/136/15/54
 J=M15c
 PS=china.ps

gmt psxy -J$J -R$R -T -K -U > $PS
 gmt psxy -R$R -J$J CHN\_adm1.gmt -K -O >> $PS
 gmt psxy -R$R -J$J HKG\_adm1.gmt -K -O >> $PS
 gmt psxy -R$R -J$J MAC\_adm0.gmt -K -O >> $PS
 gmt psxy -R$R -J$J TWN\_adm1.gmt -K -O >> $PS
 gmt psxy -R$R -J$J -T -O >> $PS
 [/code]

效果图：
 |image0|

在上一篇博文《GMT5进阶之DCW数据的使用》中利用GMT自带的DCW数据也生成了类似的图，如下图。查看全图，对比一下会发现，两张图的细节方面还是有些区别的，本文的数据绘制的似乎包含了更多的细节（主要是小的岛屿）。这个就得根据需求去选择了，当然也有可能两个都是有问题的。

.. figure:: http://ww2.sinaimg.cn/large/c27c15bejw1eapi0oct4wj21kw121n1g.jpg
   :align: center
   :alt: 

市级行政区划
^^^^^^^^^^^^

转换出来的2级数据中包含了全国所有的市级边界，用编辑器打开查看内容就会发现，每条线段都有完整的注释，很容易从众多线段中提取出自己想要的部分。以安徽省为例，将与安徽有关的线段数据保存到文件Anhui\_adm2.gmt中：
 [code lang="bash"]
 R=114/120/29/35
 J=M10c
 PS=anhui.ps

gmt psxy -J$J -R$R -T -K -U > $PS
 gmt psxy -R$R -J$J Anhui\_adm2.gmt -K -O >> $PS
 gmt psxy -R$R -J$J -T -O >> $PS
 [/code]

上面的脚本有一个很不方便的地方：想要画一个省的2级数据，每次都要从CHN\_adm2.gmt中手动提取该省的数据信息。下面的例子可以避免这种手动提取的过程，主要通过DCW数据和psclip命令，使用全国2级数据（CHN\_adm2.gmt），但是只绘制安徽省的2级数据。
 [code lang="bash"]
 R=114/120/29/35
 J=M10c
 PS=anhui.ps

gmt psxy -J$J -R$R -T -K -U > $PS
 gmt pscoast -FCN.34 -M > Anhui\_bnd.gmt
 gmt psclip -J$J -R$R Anhui\_bnd.gmt -K -O >> $PS
 gmt psxy -R$R -J$J CHN\_adm2.gmt -K -O >> $PS
 gmt psclip -C -K -O >> $PS
 gmt psxy -R$R -J$J -T -O >> $PS
 [/code]

脚本利用pscoast命令，将安徽省（代码为34）的省界数据导出到文件Anhui\_bnd.gmt中，然后利用该文件进行clip，psxy绘图时虽然使用的是全国的2级数据CHN\_adm2.gmt，但是只有安徽省内的部分会被绘制出来，最后还需要再次调用psclip以结束clip。

上面的这个脚本生成了一个中间文件Anhui\_bnd.gmt，有强迫症的人是无法忍受这个的，因而上面的代码利用管道可以进一步简化为：
 [code lang="bash"]
 R=114/120/29/35
 J=M10c
 PS=anhui.ps

gmt psxy -J$J -R$R -T -K -U > $PS
 gmt pscoast -FCN.34 -M \| gmt psclip -J$J -R$R -K -O >> $PS
 gmt psxy -R$R -J$J CHN\_adm2.gmt -K -O >> $PS
 gmt psclip -C -K -O >> $PS
 gmt psxy -R$R -J$J -T -O >> $PS
 [/code]

上面三个脚本的最终结果基本是一致的，效果图如下：

注：三个脚本的成图效果是有差的，但是目前没有体现出来，在下一段“区级行政区划”中，可以更明显地看出区别。
 |image1|

区级行政区划
^^^^^^^^^^^^

这里还是以安徽省为例，实际上只用3级数据即可，这里同时用了2级数据和3级数据，并且用不同的粗细和颜色来区分。需要注意，由于3级数据中包含了2级数据，所以下面的例子先画了3级数据，再用2级数据覆盖。如果画的顺序反了，效果就会差很多。
 [code lang="bash"]
 R=114.8/120/29.3/36
 J=M14c
 PS=anhui.ps

gmt psxy -J$J -R$R -T -K -U > $PS
 gmt psxy -R$R -J$J CHN\_adm3.gmt -W0.5p,gray -K -O >> $PS
 gmt psxy -R$R -J$J CHN\_adm2.gmt -W1p -K -O >> $PS
 gmt psxy -R$R -J$J -T -O >> $PS
 [/code]

效果图如下：
 |image2|

下面的脚本利用了前面提到的psclip的方法：
 [code lang="bash"]
 R=114.8/120/29.3/36
 J=M14c
 PS=anhui.ps

gmt psxy -J$J -R$R -T -K -U > $PS
 gmt pscoast -FCN.34 -M \| gmt psclip -J$J -R$R -K -O >> $PS
 gmt psxy -R$R -J$J CHN\_adm3.gmt -W0.5p,gray -K -O >> $PS
 gmt psxy -R$R -J$J CHN\_adm2.gmt -W1p -K -O >> $PS
 gmt psclip -C -K -O >> $PS
 gmt psxy -R$R -J$J -T -O >> $PS
 [/code]

效果图如下：
 |image3|

将这两张图对比一下，容易发现，省界的部分线段明显变细了，这算是clip的一个缺点，使用省界数据进行clip，同时又要绘制省界数据，如何判断省界数据点是否在clip区域内部是个问题。

数据本站下载
~~~~~~~~~~~~

`GADM`_\ 的版权声明如下：

    These data are freely available for academic and other
    non-commercial use. Redistribution, or commercial use, is not
    allowed without prior permission.

这里提供中国全境的转换之后的数据，可直接用于GMT绘图，需要原始shapefile的自己去官方网站下载。

数据打包下载地址，根据需求选择不同的压缩格式：

-  `China\_Adm.7z`_ 20.5M
-  `China\_Adm.tar.bz2`_ 33.2M
-  `China\_Adm.zip`_ 37.4M
-  `China\_Adm.tar.gz`_ 43M

修订历史
~~~~~~~~

-  2013-11-23：初稿；
-  2013-11-28：绘制2级和3级边界时，利用clip的方法以减少人工操作。Thanks to
   @yangtze。
-  2013-12-05：删除了数据包中的冗余隐藏文件，重新打包，提供多种格式下载。
-  2014-01-19：不推荐下载全球行政区划数据；

.. _`http://www.gadm.org/`: http://www.gadm.org/
.. _`http://www.gadm.org/country`: http://www.gadm.org/country
.. _词条: http://zh.wikipedia.org/wiki/ISO_3166-1
.. _`http://www.gadm.org/version2`: http://www.gadm.org/version2
.. _GADM: http://www.gadm.org/
.. _China\_Adm.7z: http://pan.baidu.com/s/1mZh7e
.. _China\_Adm.tar.bz2: http://pan.baidu.com/s/18DRxj
.. _China\_Adm.zip: http://pan.baidu.com/s/1y40TA
.. _China\_Adm.tar.gz: http://pan.baidu.com/s/1vMAmX

.. |image0| image:: http://ww1.sinaimg.cn/large/c27c15bejw1eaqdo86qukj21ik17fq6v.jpg
.. |image1| image:: http://ww2.sinaimg.cn/large/c27c15bejw1eaqhd9s469j211616jjtn.jpg
.. |image2| image:: http://ww2.sinaimg.cn/large/c27c15bejw1eaqemyrf9jj21d51pv44r.jpg
.. |image3| image:: http://ww1.sinaimg.cn/large/c27c15bejw1eb0p9dtlrnj21d21ptten.jpg
