Firefox安装Java插件
###################

:date: 2013-07-11 00:43
:author: SeisMan
:category: Linux
:tags: Firefox, Java
:slug: java-plugin-of-firefox

原文在\ `这里`_\ ，排版难看的要死。

操作系统：CentOS 6.4 Final

Firefox版本：17.0.7

Java版本：OpenJDK 1.7.0

1. 退出Firefox；
2. 卸载原来安装的Java插件（没装过就不卸了）；
3. 找到Java自带的浏览器插件的位置；

::

    $ locate libnpjp2
    /usr/java/jre1.7.0_21/lib/amd64/libnpjp2.so
    /usr/local/cuda-5.0/jre/lib/amd64/libnpjp2.so

4. 在firefox插件目录中建立到Java插件文件的软链接；

:: 

    $ cd ~/.mozilla/plugins/
    $ ln -s /usr/java/jre1.7.0_21/lib/amd64/libnpjp2.so libnpjp2.so

5. 启动firefox，在地址栏输入\ **about:plugins**\ ，查看插件是否正常加载；
6. 搞定收工。

.. _这里: http://www.oracle.com/technetwork/java/javase/manual-plugin-install-linux-136395.html
