利用Web Service Fetch scripts申请和下载数据
#####################################################
:date: 2013-08-04 14:19
:author: SeisMan
:category: 地震学软件
:tags: IRIS, 数据
:slug: web-service-fetch-scripts

IRIS Web Service
~~~~~~~~~~~~~~~~

IRIS
DMC提供了一系列网页服务，用于获取台站数据、仪器响应、走时以及波形数据等。简而言之，其原理大概就是根据某种特定的格式要求发送网页请求，然后IRIS会返回相应的信息供用户解析。

IRIS网页服务的主页位于：\ `http://service.iris.edu/`_\ ，有兴趣的可以研究一下。

Web Service Fetch Script
~~~~~~~~~~~~~~~~~~~~~~~~

主页：\ `https://seiscode.iris.washington.edu/projects/ws-fetch-scripts`_

这是一个利用IRIS提供的网页服务来实现数据下载的工具，其源代码用perl写成，因而几乎可以在任何平台上直接运行。整个工具包含了三个perl脚本：FetchData、FetchEvent和FetchMetadata。

FetchData
~~~~~~~~~

功能：获取时间序列文件，或/和与之相关的元数据、SAC零极点文件、响应文件。其中时间序列文件为miniSEED格式，元数据为ASCII格式。
 用法：

::

    FetchData: collect time series and related metadata (version 2013.198)
    http://service.iris.edu/clients/

    Usage: FetchData [options]

     Options:
     -v                Increase verbosity, may be specified multiple times
     -N,--net          Network code, list and wildcards (* and ?) accepted
     -S,--sta          Station code, list and wildcards (* and ?) accepted
     -L,--loc          Location ID, list and wildcards (* and ?) accepted
     -C,--chan         Channel codes, list and wildcards (* and ?) accepted
     -Q,--qual         Quality indicator, default is best
     -s starttime      Specify start time (YYYY-MM-DD,HH:MM:SS.ssssss)
     -e endtime        Specify end time (YYYY-MM-DD,HH:MM:SS.ssssss)
     --lat min:max     Specify a minimum and/or maximum latitude range
     --lon min:max     Specify a minimum and/or maximum longitude range
     --radius lat:lon:maxradius[:minradius]
                         Specify circular region with optional minimum radius
     -l listfile       Read list of selections from file
     -b bfastfile      Read list of selections from BREQ_FAST file
     -msl length       Limit returned data to a minimum segment length
     -lso              Limit returned data to the longest segment only
     -A appname        Application/version string for identification
     -a user:pass      User and password for access to restricted data

     -o outfile        Fetch time series data and write to output file
     -sd sacpzdir      Fetch SAC P&Zs and write files to sacpzdir
     -rd respdir       Fetch RESP and write files to respdir
     -m metafile       Write basic metadata to specified file

例子：获取2011年第一个小时GSN所有台站的BHZ分量的数据
 [code lang="bash"]$ FetchData -N \_GSN -C BHZ -s 2011-01-01T00:00:00 -e
2011-01-01T01:00:00 -o GSN.mseed -m GSN.metadata[/code]
 下载得到的数据为miniSEED格式，因而需要用mseed2sac进行格式转换。

说明：

-  台网、台站等支持通配符；
-  可以通过--lat和--lon划定矩形区域或通过--radius划定圆形区域来指定台站；
-  可以直接从特定格式的文件中读取要下载的波形信息；
-  可以下载相关SAC PZ文件或/和RESP文件；

FetchEvent
~~~~~~~~~~

功能：获得满足一定条件的所有事件信息
 用法：

::

    FetchEvent: collect event information (2013.198)
    http://service.iris.edu/clients/

    Usage: FetchEvent [options]

     Options:
     -v                More verbosity, may be specified multiple times (-vv, -vvv)

     -s starttime      Limit to origins after time (YYYY-MM-DD,HH:MM:SS.sss)
     -e endtime        Limit to origins before time (YYYY-MM-DD,HH:MM:SS.sss)
     --lat min:max     Specify a minimum and/or maximum latitude range
     --lon min:max     Specify a minimum and/or maximum longitude range
     --radius lat:lon:maxradius[:minradius]
                         Specify circular region with optional minimum radius
     --depth min:max   Specify a minimum and/or maximum depth in kilometers
     --mag min:max     Specify a minimum and/or maximum magnitude
     --magtype type    Specify a magnitude type for magnitude range limits
     --cat name        Limit to origins from specific catalog (e.g. ISC, PDE, GCMT)
     --con name        Limit to origins from specific contributor (e.g. ISC, NEIC)
     --ua date         Limit to origins updated after date (YYYY-MM-DD,HH:MM:SS)

     --allorigins      Return all origins, default is only primary origin per event
     --allmags         Return all magnitudes, default is only primary magnitude per event
     --orderbymag      Order results by magnitude instead of time

     --evid id         Select a specific event by DMC event ID
     --orid id         Select a specific event by DMC origin ID

     -X xmlfile        Write raw returned XML to xmlfile
     -A appname        Application/version string for identification

     -o outfile        Write event information to specified file, default: console

例子：
 [code]$ FetchEvent -s 2011-03-11 --radius 38.2:142.3:20 --mag 6[/code]
 说明：

-  这个脚本功能齐全，值得一用

FetchMetadata
~~~~~~~~~~~~~

功能：获取台站元数据
 用法：

::

    FetchMetadata: collect channel metadata (2013.198)
    http://service.iris.edu/clients/

    Usage: FetchMetadata [options]

     Options:
     -v                Increase verbosity, may be specified multiple times
     -N,--net          Network code, list and wildcards (* and ?) accepted
     -S,--sta          Station code, list and wildcards (* and ?) accepted
     -L,--loc          Location ID, list and wildcards (* and ?) accepted
     -C,--chan         Channel codes, list and wildcards (* and ?) accepted
     -s starttime      Specify start time (YYYY-MM-DD,HH:MM:SS)
     -e endtime        Specify end time (YYYY-MM-DD,HH:MM:SS)
     -ua date          Limit to metadata updated after date (YYYY-MM-DD,HH:MM:SS)
     -X xmlfile        Write raw returned FDSN StationXML to xmlfile
     -l listfile       Read list of selections from file
     -b bfastfile      Read list of selections from BREQ_FAST file
     -sta              Print station level information, default is channel
     -resp             Request response level information, no details printed
     -A appname        Application/version string for identification

     -o outfile        Write basic metadata to specified file instead of printing

其他
~~~~

整个脚本还有一些其他功能，具体参考\ `https://seiscode.iris.washington.edu/projects/ws-fetch-scripts/wiki/Running\_the\_scripts\_and\_examples`_

.. _`http://service.iris.edu/`: http://service.iris.edu/
.. _`https://seiscode.iris.washington.edu/projects/ws-fetch-scripts`: https://seiscode.iris.washington.edu/projects/ws-fetch-scripts
.. _`https://seiscode.iris.washington.edu/projects/ws-fetch-scripts/wiki/Running\_the\_scripts\_and\_examples`: https://seiscode.iris.washington.edu/projects/ws-fetch-scripts/wiki/Running_the_scripts_and_examples
