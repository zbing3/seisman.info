计算某日是一年中的第几天
########################

:date: 2014-01-18 13:33
:author: SeisMan
:category: SAC
:tags: Code
:slug: calculate-jday

该子程序根据年月日信息，计算该日为当年的第几天，主要用于给SAC文件指定发震时刻。

很久以前收集的代码片段，忘了来源在哪了。代码很粗暴，直接定义了数组@leap和@noleap，同时又相当简洁。


.. code-block:: perl

 # 
 # Input: year, month, day
 # Output: jday
 #
 
 sub cal2jul {
     my ($year, $month, $day) = @_; 
     my @noleap = qw ( 0 31 59 90 120 151 181 212 243 273 304 334 );
     my @leap   = qw ( 0 31 60 91 121 152 182 213 244 274 305 335 );
  
     if (($year%4 == 0 && $year%100 != 0) || ($year%400==0)){
         return $leap[$month-1]+$day;
     } else {
         return $noleap[$month-1]+$day;
     }   
 }
