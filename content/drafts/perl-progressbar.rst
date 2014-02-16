实现进度条的模块
#####################################################
:date: 2013-10-13 09:08
:author: SeisMan
:category: Perl
:tags: GMT脚本, 模块, 用法
:slug: perl-progressbar

Term::ProgressBar模块是一个可以用于生成进度条的Perl模块。

最小脚本，展示如何最快学会使用该模块：
 [code lang="perl"]
 #!/usr/bin/env perl

use strict;
 use warnings;
 use Term::ProgressBar 2.00;

my $max = 50000000;
 my $progress = Term::ProgressBar->new($max);

my $next\_update = 0;

for (0..$max) {
 $next\_update = $progress->update($\_) # 更新进度条
 if $\_ >= $next\_update;
 }

$progress->update($max) # 保证进度条为100%
 if $max >= $next\_update;
 [/code]

最全脚本，包含了所有功能和设置：
 [code lang="perl"]
 #!/usr/bin/env perl

use strict;
 use warnings;
 use Term::ProgressBar 2.00;

my $max = 50000000;
 my $progress = Term::ProgressBar->new({
 name => 'Counts', # 进度条名
 count => $max, # 总数
 remove => 0, # 结束后进度条是否消失
 ETA => 'linear', # 估计剩余时间,undef \|\| linear
 # major\_char => '=', # major 进度条字符
 # minor\_char => '\*', # minor 进度条字符
 # fh => \\\*STDERR, # 输出的文件句柄，\\\*STDERR \|\| \\\*STDOUT
 # term\_width => 50, # 终端宽度
 # silent => 0, # 若为1，则该模块不进行任何操作
 });

# $progress->target($max\*2); # 重定义count值
 # $progress->minor(0); # 关闭minor进度条
 # $progress->max\_update\_rate(0.5); # 两次更新的最小时间间隔(s)
 # $progress->lbrack('['); # 进度条左符号
 # $progress->rbrack(']'); # 进度条右符号

my $next\_update = 0;

for (0..$max) {
 if ( $\_ % 1000000 == 0 ) {
 $progress->message( # 输出信息，但保证进度条在输出信息的下方
 sprintf "Found %d\\n", $\_
 );
 }
 $next\_update = $progress->update($\_) # 更新进度条
 if $\_ >= $next\_update;
 }

$progress->update($max) # 保证进度条为100%
 if $max >= $next\_update;
 [/code]

参考来源：

CPAN：\ `http://search.cpan.org/~szabgab/Term-ProgressBar-2.14/lib/Term/ProgressBar.pm`_

.. _`http://search.cpan.org/~szabgab/Term-ProgressBar-2.14/lib/Term/ProgressBar.pm`: http://search.cpan.org/~szabgab/Term-ProgressBar-2.14/lib/Term/ProgressBar.pm
