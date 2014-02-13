Linux下安装TeXLive 2013
#####################################################
:date: 2013-07-11 09:00
:author: SeisMan
:category: LaTeX
:tags: 安装
:slug: texlive-2013-under-linux

安装
~~~~

下载
^^^^

下载地址：\ `http://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/texlive2013-20130530.iso`_

Linux下可以用wget、axel，windows下可以用迅雷，怎么快怎么来。

挂载
^^^^

[code lang="bash"]
 $ su
 $ mount -t  iso9660 -o loop texlive2013-20130530.iso  /mnt/
 $ cd /mnt
 $ ./install-tl
 [/code]

出现选项后，输入I直接安装（也可以更改选项）。不出意外的话，5分钟应该就OK了。

环境变量
^^^^^^^^

在.bashrc中加入如下语句：
 [code lang="bash"]
 # TeX Live 2013
 export MANPATH=${MANPATH}:/usr/local/texlive/2013/texmf-dist/doc/man
 export INFOPATH=${INFOPATH}:/usr/local/texlive/2013/texmf-dist/doc/info
 export PATH=${PATH}:/usr/local/texlive/2013/bin/x86\_64-linux
 [/code]

卸载
^^^^

[code lang="bash"]
 $ cd /
 $ sudo umount /mnt/
 [/code]

中文配置
~~~~~~~~

可以参考这篇文章：\ `http://blog.csdn.net/longerzone/article/details/8129124`_

在修改文件ctex-xecjk-winfonts.def时，[SIMKAI.TTF]替换成KaiTi，[SIMFANG.TTF]替换成FangSong.
 还可以添加更多新的字体以及Adobe字体。

.. _`http://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/texlive2013-20130530.iso`: http://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/texlive2013-20130530.iso
.. _`http://blog.csdn.net/longerzone/article/details/8129124`: http://blog.csdn.net/longerzone/article/details/8129124
