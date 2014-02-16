GMT网格数据之etopo5
#####################################################
:date: 2013-08-10 00:10
:author: SeisMan
:category: GMT
:tags: 地形, 数据, 网格
:slug: etopo5-of-gmt-grid

etopo5是全球地形及水深数据，其网格采样间隔为5弧分，目前已经被更高精度的etopo1所取代，但是在绘制大区域地形（比如全球）时，5弧分的精度已经足够，所以其依然有用武之地。官方页面位于\ `http://www.ngdc.noaa.gov/mgg/global/etopo5.html`_

下载网格数据
~~~~~~~~~~~~

[code lang="bash"]
 wget -c
http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO5/TOPO/ETOPO5/ETOPO5.DAT
 wget -c
http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO5/TOPO/ETOPO5/ETOPO5.DOS
 [/code]

ETOPO5.DAT和ETOPO5.DOS都是16位整数的二进制文件，其字节序不同。ETOPO5.DOS为little-endian，ETOPO5.DAT为big-endian。除此之外其内容完全相同。

网格数据的说明
~~~~~~~~~~~~~~

官方说明位于\ `http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO5/TOPO/ETOPO5/ETOPO5.txt`_

简单归纳一下：数据采样间隔为5弧分，经度上0度到359度55分共计4320个采样点（注意不是0到360度），维度方向-90度到90度为2161个点，每个数据为16位整数即两字节，共计4320\*2161\*2=18671040字节，但是实际上只有18662400字节，这是因为数据中把-90度的南极给丢了（不知道这是闹哪样！）。数据点顺序很简单，从北纬90度，东经0度0分开始，接下来是360度\*12采样点/度=4320采样点，即8640个字节，一直到北纬90度，东经359度55分；第4321个点为北纬89度55分，东经0度0分，按照这样的顺序不断排下去。每个维度带4320个点，共计2160个维度带。

北纬90度即北极，4320个点具有相同的值，为-4290
m；南纬-90度即南极，没有包含在这个数据中，其海拔为2810 m。

数据的小修改
~~~~~~~~~~~~

如前所说，数据里把南极丢了，这是个小问题，当绘制全球数据时会出现类似“南极海拔不一致”的警告，虽说不是致命错误，还是改了吧，源代码如下：
 [code lang="c"]
 /\*
 \* A simple C code to add the elevation of south pole to the ETOPO5
data
 \* Date: 04/30/2013
 \* Author: SeisMan @ seisman.info
 \*
 \* Input: ETOPO5.DOS
 \* Output: ETOPO5.DOS.OUT
 \* Note: ETOPO5.DOS is little-endian;
 \* ETOPO5.DAT is big-endian;
 \*/

#include<stdio.h>
 #include<stdlib.h>
 #define NX 4320
 #define NY 2160

short int \*\*imatrix(int nrl,int nrh,int ncl,int nch);

int main(){
 short int \*\*topo;
 int ix, iy;
 FILE \*fip, \*fop;

topo=imatrix(1,NX,1,NY+1);

fip=fopen("ETOPO5.DOS","rb");
 for(iy=1;iy<=NY;iy++){
 for(ix=1;ix<=NX;ix++)
 fread(&topo[ix][iy],sizeof(short int),1,fip);
 }

for(ix=1;ix<=NX;ix++)
 topo[ix][NY+1]=2810;

fop=fopen("etopo5.i2","wb");
 for(iy=1;iy<=NY+1;iy++)
 for(ix=1;ix<=NX;ix++){
 fwrite(&topo[ix][iy],sizeof(short int),1,fop);
 // printf("%d %d %d\\n",ix,iy,topo[ix][iy]);
 }

close(fip);
 close(fop);
 }

short int \*\*imatrix(int nrl,int nrh,int ncl,int nch){
 int i;
 short int \*\*m;

m=(short int \*\*)malloc((unsigned) (nrh-nrl+1)\*sizeof(short int\*));
 if (!m) fprintf(stderr,"allocation failure 1 in imatrix()\\n");
 m -= nrl;

for(i=nrl;i<=nrh;i++) {
 m[i]=(short int \*)malloc((unsigned) (nch-ncl+1)\*sizeof(short int));
 if (!m[i]) fprintf(stderr,"allocation failure 2 in imatrix()\\n");
 m[i] -= ncl;
 }
 return m;
 }[/code]
 编译并运行：

::

    gcc etopo5_mod.c -o etopo5_mod
    ./etopo5_mod

复制
~~~~

将etopo5.i2拷贝至 ${GMTHOME}/share/dbase下，其对应的grdraster.info为
 [code]1 "ETOPO5 global topography" "m" -R0/359:55/-90/90 -I5m GG i 1 0
none etopo5.i2[/code]
 也就是最原始的grdraster.info中所给的内容。

画图检查
~~~~~~~~

[code lang="bash"]
 #!/bin/bash
 verbose=-V
 #verbose=

grdraster 1 -Rg -I5m -Gout.grd $verbose
 makecpt -Cglobe -T-10500/8000/1000 -Z $verbose > colors.cpt
 grdimage out.grd -Ba60g30 -Rg -Yc -Xc -JN0/25c -Ccolors.cpt -K $verbose
> etopo5.ps
 psscale -Ba2500f500::/:"m": -Ccolors.cpt -D12.5c/-2c/15c/.35ch -O
$verbose >> etopo5.ps

rm out.grd colors.cpt
 [/code]
 |image0|
 绘图代码参考了石木说的\ `博文`_\ 。

.. _`http://www.ngdc.noaa.gov/mgg/global/etopo5.html`: http://www.ngdc.noaa.gov/mgg/global/etopo5.html
.. _`http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO5/TOPO/ETOPO5/ETOPO5.txt`: http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO5/TOPO/ETOPO5/ETOPO5.txt
.. _博文: http://hawkman.geoidea.org/2011/04/20/gmt%E7%BB%98%E5%9B%BE%E5%AD%A6%E4%B9%A0%EF%BC%9A%E7%BB%98etopo5%E4%B8%8E-etopo2%E7%BB%8F%E5%BA%A6%E7%9A%84%E5%9C%B0%E5%BD%A2%E5%9B%BE/

.. |image0| image:: http://ww3.sinaimg.cn/large/c27c15bejw1e79vh57z4bj20ne0gj77o.jpg
