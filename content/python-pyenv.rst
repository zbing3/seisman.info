Python多版本共存之pyenv
#####################################################
:date: 2013-10-04 00:27
:author: SeisMan
:category: Python
:tags: 安装
:slug: python-pyenv

与\ `《Perl多版本共存》`_\ 的原因类似，需要在系统里安装Python的其他版本，而不影响到系统自带的Python。

Perl里有perlbrew可以很好的解决Perl多版本共存的问题，Python里也有一个类似的工具---\ `pythonbrew`_\ 。其项目主页里说

    This project is no longer under active development.
     You are encouraged to try out `pyenv`_ instead.

决定使用\ `pyenv`_\ 。详细的信息参见\ `pyenv`_\ 的项目主页，下面记录下安装过程。

安装pyenv
~~~~~~~~~

获取pyenv代码
^^^^^^^^^^^^^

使用使用git获取pyenv源码，默认安装到~/.pyenv下。

::

    $ cd
    $ git clone git://github.com/yyuu/pyenv.git .pyenv

定义环境变量
^^^^^^^^^^^^

添加环境变量PYENV\_ROOT到.bashrc，并修改PATH。

::

    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

加入pyenv init
^^^^^^^^^^^^^^

pyenv init实际上做了很多事情，具体不说。

::

    $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc

重启SHELL
^^^^^^^^^

::

    $ exec $SHELL

至此pyenv安装完毕，且配置完成。

安装Python
~~~~~~~~~~

使用如下命令即可安装python 3.3.2.

::

    $ pyenv install 3.3.2

该命令会从github上下载python的源代码，并解压到/tmp目录下，然后在/tmp中执行编译工作。编译过程依赖一些其他的库文件，若库文件不能满足，则编译错误，需要重新下载、编译。。。(为什么每次都要重新下呢？)

已知的一些需要预先安装的库包括：

-  readline readline-devel readline-static
-  openssl openssl-devel openssl-static
-  sqlite-devel
-  bzip2-devel bzip2-libs

在所有python依赖库都安装好的情况下，python的安装很顺利：

::

    $ pyenv install 3.3.2
    Downloading Python-3.3.2.tgz...
    -> http://yyuu.github.io/pythons/0a2ea57f6184baf45b150aee53c0c8da
    Installing Python-3.3.2...
    Installed Python-3.3.2 to /export/home/seisman/.pyenv/versions/3.3.2

    Downloading setuptools-1.1.4.tar.gz...
    -> https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.4.tar.gz
    Installing setuptools-1.1.4...
    Installed setuptools-1.1.4 to /export/home/seisman/.pyenv/versions/3.3.2

    Downloading pip-1.4.1.tar.gz...
    -> https://pypi.python.org/packages/source/p/pip/pip-1.4.1.tar.gz
    Installing pip-1.4.1...
    Installed pip-1.4.1 to /export/home/seisman/.pyenv/versions/3.3.2

Rehash
^^^^^^

相当于更新一下数据库：

::

    $ pyenv rehash

查看当前已安装的python版本
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    $ pyenv versions
    * system (set by /export/home/seisman/.pyenv/version)
    3.3.2

其中的星号表示使用的是系统自带的python。

设置全局的python版本
^^^^^^^^^^^^^^^^^^^^

::

    $ pyenv global 3.3.2
    $ pyenv versions
    system
    * 3.3.2 (set by /export/home/seisman/.pyenv/version)

当前全局的python版本已经变成了3.3.2。也可以使用\ ``pyenv local``\ 或\ ``pyenv shell``\ 临时改变python版本。

确认python版本
^^^^^^^^^^^^^^

::

    $ python
    Python 3.3.2 (default, Sep 30 2013, 20:11:44) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

安装pyenv-virtualenv
~~~~~~~~~~~~~~~~~~~~

pyenv-virtualenv不装也没问题

安装完新版的python之后，其实就已经可以用了。使用pip安装第三方模块时是安装到~/.pyenv/versions/3.3.2下的，所以不会和系统模块有冲突。为什么需要pyenv-virtual呢?

安装
^^^^

::

    $ git clone git://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

建立虚拟环境
^^^^^^^^^^^^

其中3.3.2是已安装的python版本号，my-virtual-env-3.3.2是虚拟环境名。

::

    $ pyenv virtualenv 3.3.2 my-virtual-env-3.3.2

该命令会在~/.pyenv/versions下建立my-virtual-env-3.3.2目录，并安装setuptools、pip等。默认从(\ `https://bitbucket.org/pypa/setuptools/downloads/ez\_setup.py)获取代码，但是不知为何这个网址无法链接，所以安装一直不成功。`_

需要在终端设置如下环境变量，再执行创建虚拟环境即可：

::

    $ export SETUPTOOLS_VERSION=bootstrap
    $ pyenv virtualenv 3.3.2 my-virtual-env-3.3.2

切换至虚拟环境
^^^^^^^^^^^^^^

创建虚拟环境完成后

::

    $ pyenv global my-virtual-env-3.3.2

则切换到虚拟环境。

使用python
~~~~~~~~~~

-  输入\ ``python``\ 即可使用新版本的python；
-  系统命令会以/usr/bin/python的方式直接调用老版本的python；
-  使用pip安装第三方模块时会安装到~/.pyenv/versions/3.3.2下，不会和系统模块发生冲突。

.. _《Perl多版本共存》: http://seisman.info/perlbrew-for-multiple-versions-of-perl.html
.. _pythonbrew: https://github.com/utahta/pythonbrew
.. _pyenv: https://github.com/yyuu/pyenv
.. _`https://bitbucket.org/pypa/setuptools/downloads/ez\_setup.py)获取代码，但是不知为何这个网址无法链接，所以安装一直不成功。`: https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py)%E8%8E%B7%E5%8F%96%E4%BB%A3%E7%A0%81%EF%BC%8C%E4%BD%86%E6%98%AF%E4%B8%8D%E7%9F%A5%E4%B8%BA%E4%BD%95%E8%BF%99%E4%B8%AA%E7%BD%91%E5%9D%80%E6%97%A0%E6%B3%95%E9%93%BE%E6%8E%A5%EF%BC%8C%E6%89%80%E4%BB%A5%E5%AE%89%E8%A3%85%E4%B8%80%E7%9B%B4%E4%B8%8D%E6%88%90%E5%8A%9F%E3%80%82
