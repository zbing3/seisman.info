USTC网络通登录脚本
##################

:date: 2014-01-08 20:04
:author: SeisMan
:category: Perl
:tags: Code
:slug: ustc-wlt-login

脚本来源：\ `https://lug.ustc.edu.cn/wiki/scripts/wlt`_\ ，略有修改和简化。

.. code-block:: perl

 #!/usr/bin/env perl
 #
 # Perl Script to login wlt.ustc.edu.cn
 # https://lug.ustc.edu.cn/wiki/scripts/wlt
 #
 use warnings;

 # user name and password
 $name="xxxxxxx";
 $password="xxxxxxxx";

 $wget="/usr/bin/wget";
 $url="http://wlt.ustc.edu.cn/cgi-bin/ip";
 $log="/dev/null";
 $page="/tmp/wlt_state";
 $cookies="/tmp/wlt_cookies";

 @type=( "教育网出口(国际,仅用教育网访问,适合看文献)",
 "电信网出口(国际,到教育网走教育网)",
 "联通网出口(国际,到教育网走教育网)",
 "电信网出口2(国际,到教育网免费地址走教育网)",
 "联通网出口2(国际,到教育网免费地址走教育网)",
 "电信网出口3(国际,到教育网走教育网,到联通走联通)",
 "联通网出口3(国际,到教育网走教育网,到电信走电信)",
 "教育网国际出口(国际,国内使用电信和联通,国际使用教育网)",
 "移动测试国际出口(国际,无P2P或带宽限制)");
 @exp= ( 0, 120, 3600, 14400, 39600, 50400);
 @expstr=("永久", "动态", "1小时", "4小时, 缺省", "11小时", "14小时");

 # 登录网络通，用--keep-session-cookies和--save-cookies得到Cookies
 $cmd="cmd=login";
 # 这个输出页面不需要，只需要得到cookies
 $options="-o $log -O $log --keep-session-cookies --save-cookies
 $cookies --post-data '$cmd&name=$name&password=$password'";
 system "$wget $options $url";

 print "请选择出口：\n";
 $i=0;
 foreach (@type) {
     print "\t", $i+1, ": $type[$i]\n";
     $i=$i+1;
 }
 print "注：选择出口2、3无法使用的某些电子资源，使用出口4、5、6可能可以正常使用\n";
 do {
     print "[1-9] ";
     $type=<STDIN>;
 } while ($type<1 || $type >9);
 $type -= 1;

 print "使用时限：\n";
 $i=0;
 foreach (@exp) {
     print "\t", $i+1, ": $exp[$i]s, $expstr[$i]\n";
     $i=$i+1;
 }
 do {
     print "[1-6] ";
     $exp=<STDIN>;
 } while ($exp<1 || $exp>9);
 $exp -= 1;

 $expstr=$expstr[$exp];
 $exp=$exp[$exp];

 $cmd="cmd=set";
 # 利用Cookies选择出口和时限
 $options="-o $log -O $page --load-cookies $cookies --post-data \"$cmd&name=$name&password=$password&type=$type&exp=$exp\"";
 system "$wget $options $url";

脚本名为wlt.pl，位于${HOME}/bin下，权限设置为“500”。

.. _`https://lug.ustc.edu.cn/wiki/scripts/wlt`: https://lug.ustc.edu.cn/wiki/scripts/wlt
