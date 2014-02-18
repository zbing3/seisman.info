判断字节序的多种方法
#####################################################
:date: 2013-11-13 00:33
:author: SeisMan
:category: Linux
:tags: endian
:slug: linux-endian

本文整理自：\ `http://serverfault.com/questions/163487/linux-how-to-tell-if-system-is-big-endian-or-little-endian`_

直接查看系统文件：
 [code lang="bash"]
 lscpu \| grep -i byte
 [/code]

Bash版：
 [code lang="bash"]echo -n I \| od -to2 \| head -n1 \| cut -f2 -d" " \|
cut -c6[/code]
 若输出为1则为Little Endian，若输出为0则为Big Endian。

为了适应不同操作系统的需求，还有其他各种变种：
 [code lang="bash"]echo I \| tr -d [:space:] \| od -to2 \| head -n1 \|
awk '{print $2}' \| cut -c6[/code]
 [code lang="bash"]echo -n I \| od -to2 \| awk '{ print substr($2,6,1);
exit}'[/code]
 [code lang="bash"]echo -n I \| hexdump -o \| awk '{ print
substr($2,6,1); exit}'[/code]

Python一行命令版：
 [code lang="python"]
 python -c "import sys;print(0 if sys.byteorder=='big' else 1)"
 [/code]

Python脚本版：
 [code lang="python"]
 #!/usr/bin/env python
 from struct import pack
 if pack('@h', 1) == pack('<h', 1):
 print "Little Endian"
 else:
 print "Big Endian"
 [/code]

Jython脚本版：
 [code lang="java"]
 from java.lang import System
 for property, value in dict(System.getProperties()).items():
 if property.endswith('cpu.endian'):
 return value
 [/code]

.. _`http://serverfault.com/questions/163487/linux-how-to-tell-if-system-is-big-endian-or-little-endian`: http://serverfault.com/questions/163487/linux-how-to-tell-if-system-is-big-endian-or-little-endian
