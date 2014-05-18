Python科学计算发行版--Anaconda
##############################

:date: 2014-05-14 13:00
:author: SeisMan
:category: Python
:slug: anaconda-scientific-python-distribution

Python是一种强大的编程语言，其提供了很多模块，可以用于科学计算，常见的包括numpy、scipy和matplotlib。要利用Python进行科学计算，就需要一一安装所需的模块，而这些模块可能又依赖于其它的软件包或库，因而安装和使用起来相对麻烦。于是各种科学计算发行版就诞生了，Anaconda就是其中一个。

主页：https://store.continuum.io/cshop/anaconda/

Anaconda的特点：

- 包含了众多流行的科学、数学、工程、数据分析的Python包 http://docs.continuum.io/anaconda/pkgs.html
- 完全开源和免费
- 额外的加速、优化是收费的，但对于学术用途可以申请免费的License
- 全平台支持：Linux、Windows、Mac
- 支持Python 2.6、2.7、3.3，可自由切换

安装
====

#. 下载 http://continuum.io/downloads
#. 安装

   .. code-block:: bash

      $ bash Anaconda-1.x.x-Linux-x86[_64].sh

#. 使用Python3

   anaconda默认的Python版本是2.7.6，若需要使用Python3.3，需要额外安装。

   .. code-block:: bash

      $ conda create -n py3k python=3 anaconda

#. 切换至Python3

   .. code-block:: bash
    
      $ source activate py3k

#. 申请免费的学术License

   https://store.continuum.io/cshop/academicanaconda

#. 安装额外的功能包

   .. code-block:: bash

      $ conda update conda    
      $ conda install accelerate    
      $ conda install iopro
