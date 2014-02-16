Perl多版本共存之plenv
#####################################################
:date: 2013-11-03 01:24
:author: SeisMan
:category: Perl
:tags: 安装
:slug: perl-plenv

前面写了两篇相关的文章。

`《Perl多版本共存之Perlbrew》`_\ 中介绍了如何用Perlbrew实现多个Perl版本的共存。

`《Python多版本共存之pyenv》`_\ 中介绍了如何使用pyenv实现多个Python版本的共存。

Perlbrew在Python下有个对应的工具叫做Pythonbrew，只是因为各种原因目前已经不再开发了。

pyenv在Perl下也有个对应的工具，叫做plenv，根据官方的说法，其比perlbrew要更方便好用。

官方网站：\ `https://github.com/tokuhirom/plenv`_

其用法与pyenv类似，下面只列出基本步骤，具体介绍参见以前的博文和官方的介绍。

[code lang="bash"]
 $ git clone git://github.com/tokuhirom/plenv.git ~/.plenv
 $ echo 'export PATH="$HOME/.plenv/bin:$PATH"' >> ~/.bashrc
 $ echo 'eval "$(plenv init -)"' >> ~/.bashrc
 $ exec $SHELL -l
 $ git clone git://github.com/tokuhirom/Perl-Build.git
~/.plenv/plugins/perl-build/
 $ plenv install --list
 $ plenv install 5.18.1
 $ plenv rehash
 $ plenv versions
 $ plenv global 5.18.1
 $ plenv install-cpanm
 [/code]

.. _《Perl多版本共存之Perlbrew》: http://seisman.info/perlbrew-for-multiple-versions-of-perl.html
.. _《Python多版本共存之pyenv》: http://seisman.info/python-pyenv.html
.. _`https://github.com/tokuhirom/plenv`: https://github.com/tokuhirom/plenv
