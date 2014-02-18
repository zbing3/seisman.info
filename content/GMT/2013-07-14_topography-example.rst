GMT绘制高精度地形图的一个例子
#############################

:date: 2013-07-14 16:59
:author: SeisMan
:category: GMT
:tags: GMT技巧, GMT脚本, GMT4
:slug: topography-example

.. contents::

说明
====
该脚本可以成功运行并绘图，但仅限于此例，脚本本身不具备可复用性。

列举已知bug如下：

- 该脚本中的经度为三位整数，不支持两位整数或1位整数；
- 该脚本中数据位于北纬东经，对于南纬或者西经，需要考虑负号；
- 该脚本中采用循环grdpaste实现网格合并，想法不错，但过于复杂，用grdblend更合适；

脚本改起来不难，该脚本的核心在于如何循环调用xyz2grd以及grdpaste命令来生成网格，但，中国科学院计算机网络信息中心提供了5度*5度的SRTM3数据，数据转换更容易，详情参考这篇\ `博文 <{filename}/GMT/srtm.rst>`_\ 。因而该脚本已经没有存在的意义了。

由来
====

我一般用GMT画图都是画全球或大区域图，所以地形ETOPO2差不多就已经够我用了。前几日妹子野外实习有个答辩，让我帮忙找一张中印边境的山脉图。网上找了下，没有合心意的；试了下Google地球，清晰度不太够；想想还是在妹子面前秀一下，自己画一张地图好了。用了两个小时左右时间写脚本画图，然后调各种参数，出来的图我自己不太满意，妹子说可以用。好吧，要求真低。答辩完了，图和数据都可以删了。回顾了一下，其实脚本里还是有一些不错的思路在里面，所以就写在这里了。

脚本1：数据下载
===============

采用的数据是SRTM3，其精度为3"，也就是90m一个格点。这精度相当高，同时也使得数据文件相当大。

感兴趣的范围是经度100-106，纬度21-26。下面的脚本对经纬度进行循环，构建文件名，然后用axel下载。（Linux下一般用wget下载，axel支持多线程，下载速度快，偶尔用一下也不错）。
 
.. code-block:: perl
 
 #!/usr/bin/perl -w

 $xmin = 100;
 $xmax = 106;
 $ymin = 21;
 $ymax = 26;

 for ($ix=$xmin; $ix<=$xmax; $ix++){
     for ($iy=$ymin; $iy<=$ymax; $iy++){
         $file = "N".$iy."E".$ix.".hgt.zip";
         system "axel -n 4 http://dds.cr.usgs.gov/srtm/version2\_1/SRTM3/Eurasia/$file";
         system "unzip $file";
     }
 }

脚本2：绘图
===========

整个脚本其实很简单，利用Perl强大的字符处理和数值运算能力实现循环，将整个过程完全脚本化。

.. code-block:: perl

 #!/usr/bin/perl -w

 use strict;
 my $J="M6i";
 my $xmin = 100;
 my $xmax = 106;
 my $ymin = 21;
 my $ymax = 26;

 my $R="$xmin/$xmax/$ymin/$ymax";
 my $B="1/1WSEN";
 my $PS="template.ps";

 &GMT_open($J, $R, $PS);

 # 将下载解压得到的数据转换成GMT网格文件
 for (my $ix=$xmin; $ix<=$xmax; $ix++){
     for (my $iy=$ymin; $iy<=$ymax; $iy++){
         my $name = "N".$iy."E".$ix;
         my $hgt = $name.".hgt";
         my $grd = $name.".grd";
         my $ixx = $ix+1;
         my $iyy = $iy+1;
         my $range = "$ix/$ixx/$iy/$iyy";
         system "xyz2grd $hgt -G$grd -I3c -R$range -N-32768 -ZTLhw -V";
     }
 }
 # 对GMT网格文件进行paste，这里是横向paste
 for (my $iy=$ymin; $iy<=$ymax; $iy++){
     my $firstgrd = "N".$iy."E".$xmin.".grd";
     for (my $ix=$xmin+1; $ix<=$xmax; $ix++){
         my $secondgrd = "N".$iy."E".$ix.".grd";
         system "grdpaste $firstgrd $secondgrd -G$firstgrd -V";
         unlink $secondgrd;
     }
 }
 # 对网格文件进行纵向paste
 my $firstgrd = "N".$ymin."E".$xmin.".grd";
 for (my $iy=$ymin+1; $iy<=$ymax; $iy++){
     my $secondgrd = "N".$iy."E".$xmin.".grd";
     system "grdpaste $firstgrd $secondgrd -G$firstgrd -V";
     unlink $secondgrd;
 }

 my $finalgrd = "N".$ymin."E".$xmin.".grd";
 my $grdint = $finalgrd."int";
 # nrwc.cpt来自于http://soliton.vm.bytemark.co.uk/pub/cpt-city/
 system "grd2cpt $finalgrd -Cnrwc.cpt -Z > colors.cpt";
 system "grdgradient $finalgrd -A120 -G$grdint -M";
 system "grdimage $finalgrd -B$B -R$R -J$J -I$grdint -Ccolors.cpt -K -O >> $PS";
 system "pscoast -R$R -J$J -B$B -Df -N1/1p -W1p/black -K -O >> $PS";

 open (PSXY, "| psxy -J$J -R$R -Sc0.1c -W1p/red -Gred -K -O >> $PS");
 print PSXY "101.327 24.215 \n";
 print PSXY "104.225 23.378 \n";
 print PSXY "103.795 22.813 \n";
 print PSXY "103.227 22.780 \n";
 print PSXY "102.084 22.952 \n";
 close(PSXY);

 open(PSTEXT, "| pstext -R$R -J$J -K -O -N >> $PS");
 print PSTEXT "101.327 24.215 10 0 2 2 Mount. Ailao \n";
 print PSTEXT "104.225 23.378 10 0 2 2 Mount. Laojun \n";
 print PSTEXT "103.795 22.813 10 0 2 2 Mount. Dawei \n";
 print PSTEXT "103.227 22.780 10 0 2 2 Mount. Xilong \n";
 print PSTEXT "102.084 22.952 10 0 2 2 Mount. Qilian \n";
 close(PSTEXT);

 &GMT_close($J, $R, $PS);

 sub GMT_open {
     my ($J, $R, $PS ) = @_;
     system("psxy -J$J -R$R < /dev/null -K > $PS");
 }

 sub GMT_close {
     my ($J, $R, $PS ) = @_;
     system("psxy -J$J -R$R < /dev/null -O >> $PS");
 }


效果图
======

图的精度足够，可以看到很多的细节。但是整体色调还是不理想。

.. figure:: http://ww2.sinaimg.cn/large/c27c15bejw1e8w9zn2kybj21kw1e2kjl.jpg
   :alt: SRTM3效果图 
   :width: 700 px

修订历史
========

- 2013-07-14：初稿；
- 2013-09-23：加入最终成图；
