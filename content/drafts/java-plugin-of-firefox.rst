Firefox安装Java插件
#####################################################
:date: 2013-07-11 00:43
:author: SeisMan
:category: Linux
:tags: Firefox, Java
:slug: java-plugin-of-firefox

原文在\ `这里`_\ ，排版难看的要死。

操作系统：CentOS 6.4 Final

Firefox版本：17.0.7

Java版本：OpenJDK 1.7.0

-  退出Firefox；
-  卸载原来安装的Java插件（没装过就不卸了）；
-  找到Java自带的浏览器插件的位置；
    [code lang="bash"]
    $ locate libnpjp2
    /usr/java/jre1.7.0\_21/lib/amd64/libnpjp2.so

   /usr/local/Wolfram/Mathematica/8.0/SystemFiles/Java/Linux/lib/i386/libnpjp2.so
    /usr/local/cuda-5.0/jre/lib/amd64/libnpjp2.so
    [/code]
-  在firefox插件目录中建立到Java插件文件的软链接；
    [code lang="bash"]
    $ cd ~/.mozilla/plugins/
    $ ln -s /usr/java/jre1.7.0\_21/lib/amd64/libnpjp2.so libnpjp2.so
    [/code]
-  启动firefox，在地址栏输入\ **about:plugins**\ ，查看插件是否正常加载；
-  搞定收工。

.. _这里: http://www.oracle.com/technetwork/java/javase/manual-plugin-install-linux-136395.html
