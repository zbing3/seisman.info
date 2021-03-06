SAC二进制版的安装
#################

:date: 2013-07-08 20:30
:modified: 2014-02-17
:author: SeisMan
:category: SAC
:tags: 安装
:slug: install-sac-from-binary-package

.. contents::

申请
====

SAC是一个免费软件，但是其需要申请才可以获得。下面给出了申请网址，\ **认真填写**\ ，邮箱尽量用学校或单位邮箱，至少是个专业点的邮箱（163、QQ邮箱好像都有被拒的经历）。在平台选择处选择Linux 64位（如果有兴趣也可以选择一个source
code）。若验证通过，三个工作日内即可收到附件中还有软件包的邮件。

申请网址：\ `http://www.iris.edu/forms/sac\_request.htm`_

解压
====

对sac软件包直接解压，会出现sac文件夹，里面包含了多个文件夹：

.. code-block:: bash
    
    tar -zxvf sac-101.6-linux_x86_64.tar.gz

安装
====

这里使用的是SAC的二进制版，因而不需要编译。将整个sac
文件夹拷到某目录下（SAC 推荐安装目录为/usr/local）：

.. code-block:: bash

    sudo cp -r sac /usr/local

设置环境变量
============

修改\ ``~/.bashrc``\ ，加入环境变量申明。这里分为基础版和高级版两种方式，基础版可以保证SAC可以使用，高级版提供了更多的可定制参数，按需选择。

基础版
------

向.bashrc中加入如下语句：

.. code-block:: bash
 
 export SACHOME=/usr/local/sac
 export SACAUX=$SACHOME/aux
 export PATH=$SACHOME/bin:$PATH

高级版
------

向.bashrc中加入如下语句：

.. code-block:: bash

 export SACHOME=/usr/local/sac
 export PATH=${PATH}:${SACHOME}/bin
 export SACAUX=${SACHOME}/aux
 export SAC_DISPLAY_COPYRIGHT=1
 export SAC_USE_DATABASE=1
 export SAC_PPK_LARGE_CROSSHAIRS=1
 alias sac="${SACHOME}/bin/sac /usr/local/sac/aux/init.m"

在/usr/local/sac/aux中创建新文件init.m，其内容为

.. code-block:: bash

 qdp off;

使环境变量生效
==============

终端输入

.. code-block:: bash

    source ~/.bashrc

启动SAC
=======

终端输入sac（注意要小写），看到版本号等信息即安装成功。

.. code-block:: bash

 $ sac
 SEISMIC ANALYSIS CODE [06/12/2013 (Version 101.6)]
 Copyright 1995 Regents of the University of California

 SAC>

环境变量的说明
==============

- SACHOME是一个自定义变量，代表SAC的位置；
- SACAUX是SAC运行过程中需要的辅助文件的位置；
- PATH是将SAC的可执行文件路径加入到shell的搜索路径中；
- SAC_DISPLAY_COPYRIGHT可以取0或1，表示是否显示版权信息，在批处理数据调用SAC的时候这个最好设置为0；
- SAC_USE_DATABASE可以取0和1，忘记是干嘛的了；
- SAC_PPK_LARGE_CROSSHAIRS可以取0或1，在使用ppk挑震相的时候用到，个人建议选择1；
- alias使得sac在启动的时候执行初始化脚本init.m，SAC在启动后首先执行init.m内的命令；
- init.m的内容可以根据需要修改，/usr/local/sac/README中有具体例子；我个人目前之使用了\ ``qdp off``\ ；

备注
====

启动SAC时可能会出现如下错误:

::

    sac: error while loading shared libraries: libXpm.so.4: cannot open shared object file: No such file or directory

这是因为缺少了动态链接库\ ``libXpm.so.4``\ 的缘故，需要安装Xpm相关包。

::

    yum install libXpm-devel

修订历史
========
2013-07-08：初稿;
2014-02-17：加入了关于\ ``libXpm``\ 的说明；

.. _`http://www.iris.edu/forms/sac\_request.htm`: http://www.iris.edu/forms/sac_request.htm
