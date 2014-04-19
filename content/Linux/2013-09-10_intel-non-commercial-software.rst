Intel 非商业开发工具安装记录
############################

:date: 2013-09-10 11:39
:author: SeisMan
:category: Linux
:tags: 安装
:slug: intel-non-commercial-software

.. contents::

Intel网址：\ `http://software.intel.com/en-us/non-commercial-software-development`_

Intel® Parallel Studio XE 2013包含了C、Fortran编译器、MKL数学库以及性能分析工具。在填写一些必要的信息之后即可下载，同时Intel会向注册邮箱内发送license，有效期一年，一年后需要重新申请。

解压
====

.. code-block:: bash

 $ tar -zxvf parallel_studio_xe_2013_update3_intel64.tgz
 $ cd parallel_studio_xe_2013_update3_intel64
 $ su
 # ./install.sh

初始化
======

::

    --------------------------------------------------------------------------------
    Initializing, please wait...
    --------------------------------------------------------------------------------

欢迎界面
========

::

    Step no: 1 of 7 | Welcome
    --------------------------------------------------------------------------------
    Welcome to the Intel(R) Parallel Studio XE 2013 Update 3 for Linux* installation
    program.
    --------------------------------------------------------------------------------
    You will complete the steps below during this installation:
    Step 1 : Welcome
    Step 2 : License
    Step 3 : Activation
    Step 4 : Intel(R) Software Improvement Program
    Step 5 : Options
    Step 6 : Installation
    Step 7 : Complete
    --------------------------------------------------------------------------------
    Press "Enter" key to continue or "q" to quit: 

检测依赖性
==========

::

    Step no: 1 of 7 | Options > Missing Optional Pre-requisite(s)
    --------------------------------------------------------------------------------
    There are one or more optional unresolved issues. It is highly recommended to
    resolve them all before you continue the installation. You can fix them without 
    exiting from the installation and re-check. Or you can quit from the
    installation, fix them and run the installation again.
    --------------------------------------------------------------------------------
    Missing optional pre-requisites
    -- Intel(R) Composer XE 2013 Update 3 for Linux*: unsupported OS
    --------------------------------------------------------------------------------
    1. Skip missing optional pre-requisites [default]
    2. Show the detailed info about issue(s)
    3. Re-check the pre-requisites

    h. Help
    b. Back to the previous menu
    q. Quit
    --------------------------------------------------------------------------------
    Please type a selection or press "Enter" to accept default choice [1]: 2

显示不支持当前操作系统。

::

    Step no: 1 of 7 | Options > Missing Optional Pre-requisite
    --------------------------------------------------------------------------------
    Intel(R) Composer XE 2013 Update 3 for Linux*: Detected operating system is not 
    supported. Supported operating systems for this release include:
        - Red Hat Enterprise Linux* 5.0, 6.0 (IA-32/Intel(R) 64)
        - Fedora* 17 (IA-32/Intel(R) 64)
        - SuSE Linux* Enterprise Server* 10, 11 SP2 (IA-32/Intel(R)64)
        - Ubuntu* 11.10, 12.04 (IA-32/Intel(R) 64)
        - Debian* 6 (IA-32/Intel(R) 64)
        - Pardus* 2011.2 (Intel(R) 64)
    --------------------------------------------------------------------------------
    1. Finish with prerequisites and continue installation [default]
    2. Back to Pre-requisite summary dialog

    h. Help
    b. Back to the previous menu
    q. Quit
    --------------------------------------------------------------------------------
    Please type a selection or press "Enter" to accept default choice [1]: 1

我的系统是CentOS 6.4 x86\_64，与Red Hat 6.0基本是一样的，所以这个“操作系统不支持”的问题可以忽略。

License
=======

::

    Step no: 2 of 7 | License
    --------------------------------------------------------------------------------
    一堆英文。。。
    --------------------------------------------------------------------------------
    Do you agree to be bound by the terms and conditions of this license agreement?
    Type "accept" to continue or "decline" to back to the previous menu: accept      

激活
====

::

    Step no: 3 of 7 | Activation
    --------------------------------------------------------------------------------
    If you have purchased this product and have the serial number and a connection
    to the internet you can choose to activate the product at this time. Activation
    is a secure and anonymous one-time process that verifies your software licensing
    rights to use the product. Alternatively, you can choose to evaluate the
    product or defer activation by choosing the evaluate option. Evaluation software
    will time out in about one month. Also you can use license file, license
    manager, or remote activation if the system you are installing on does not 
    have internet access activation options.
    --------------------------------------------------------------------------------
    1. I want to activate my product using a serial number [default]
    2. I want to evaluate my product or activate later 
    3. I want to activate either remotely, or by using a license file, or by using a
       license manager

    h. Help
    b. Back to the previous menu
    q. Quit
    --------------------------------------------------------------------------------
    Please type a selection or press "Enter" to accept default choice [1]: 1            

    Please type your serial number (the format is XXXX-XXXXXXXX): 查看邮箱找激活码
    --------------------------------------------------------------------------------
    Activation completed successfully.
    --------------------------------------------------------------------------------
    Press "Enter" key to continue: 

Intel软件提升计划
=================

::

    Step no: 4 of 7 | Intel(R) Software Improvement Program 
    --------------------------------------------------------------------------------
    Help improve your experience with Intel(R) software
         
    Participate in the design of future Intel software. Select 'Yes' to give us
    permission to learn about how you use your Intel software and we will do the
    rest.
        - No Personal contact information is collected
        - There are no surveys or additional follow-up emails by opting in
        - You can stop participating at any time
             
        Learn more about Intel(R) Software Improvement Program
        http://software.intel.com/en-us/articles/software-improvement-program

    With your permission, Intel may automatically receive anonymous information 
    about how you use your current and future Intel software.
    --------------------------------------------------------------------------------
    1. Yes, I am willing to participate and improve Intel software. (Recommended)
    2. No, I don't want to participate in the Intel(R) Software Improvement Program
       at this time.

    b. Back to the previous menu
    q. Quit
    --------------------------------------------------------------------------------
    Please type a selection: 1

安装选项
========

::

    Step no: 5 of 7 | Options
    --------------------------------------------------------------------------------
    You are now ready to begin installation. You can use all default installation
    settings by simply choosing the "Start installation Now" option or you can
    customize these settings by selecting any of the change options given below
    first. You can view a summary of the settings by selecting 
    "Show pre-install summary".
    --------------------------------------------------------------------------------
    1. Start installation Now

    2. Change install directory      [ /opt/intel ]
    3. Change components to install  [ All ]
    4. Change advanced options
    5. Show pre-install summary

    h. Help
    b. Back to the previous menu
    q. Quit
    --------------------------------------------------------------------------------
    Please type a selection or press "Enter" to accept default choice [1]: 1

默认就好。

正式安装
========

::

    Step no: 6 of 7 | Installation
    --------------------------------------------------------------------------------
    Each component will be installed individually. If you cancel the installation,
    components that have been completely installed will remain on your system. This
    installation may take several minutes, depending on your system and the options
    you selected.
    --------------------------------------------------------------------------------
    Installing Amplifier XE Command line interface component... done
    --------------------------------------------------------------------------------
    Installing Amplifier XE Sampling driver kit component...
      WARNING: NMI watchdog timer is enabled. 
    Suggestion: turn off the nmi_watchdog timer before running sampling. 
    --------------------------------------------------------------------------------
    Installing Amplifier XE Power driver kit component...
      WARNING: Failed to load driver into the kernel. 
    Suggestion: after the installation completes, see
    '/opt/intel/vtune_amplifier_xe_2013/powerdk/src/README.txt' for information on
    how to build and load the driver into the kernel. 
    --------------------------------------------------------------------------------
    Installing Amplifier XE Graphical user interface component... done
    --------------------------------------------------------------------------------
    Installing Inspector XE Command line interface component... done
    --------------------------------------------------------------------------------
    Installing Inspector XE Graphical user interface component... done
    --------------------------------------------------------------------------------
    Installing Advisor XE Command line interface component... done
    --------------------------------------------------------------------------------
    Installing Advisor XE Graphical user interface component... done
    --------------------------------------------------------------------------------
    Installing Intel Fortran Compiler XE 13.1 Update 1 on Intel(R) 64 component... done
    --------------------------------------------------------------------------------
    Installing Intel C++ Compiler XE 13.1 Update 1 on Intel(R) 64 component... done
    --------------------------------------------------------------------------------
    Installing Intel Debugger 13.0 on Intel(R) 64 component... done
    --------------------------------------------------------------------------------
    Installing Intel Math Kernel Library 11.0 Update 3 on Intel(R) 64 component...
    Installing Intel Integrated Performance Primitives 7.1 Update 1 on Intel(R) 64
    component... done
    --------------------------------------------------------------------------------
    Installing Intel Threading Building Blocks 4.1 Update 3 core files and examples 
    component... done
    --------------------------------------------------------------------------------
    Finalizing installation... done
    --------------------------------------------------------------------------------

安装完成
========

::

    Step no: 7 of 7 | Complete
    --------------------------------------------------------------------------------
    Thank you for installing and using the
    Intel(R) Parallel Studio XE 2013 Update 3 for Linux*

    Reminder: Intel(R) VTune(TM) Amplifier XE users must be members of the "vtune" 
    permissions group in order to use Event-based Sampling.

    To register your product purchase, visit
    https://registrationcenter.intel.com/RegCenter/registerexpress.aspx?clientsn=N43
    3-3FHWSF85
        
    To get started using Intel(R) VTune(TM) Amplifier XE 2013 Update 5:
        - To set your environment variables: source
    /opt/intel/vtune_amplifier_xe_2013/amplxe-vars.sh
        - To start the graphical user interface: amplxe-gui
        - To use the command-line interface: amplxe-cl
        - For more getting started resources: /opt/intel/vtune_amplifier_xe_2013/
          documentation/en/welcomepage/get_started.html.
    To get started using Intel(R) Inspector XE 2013 Update 5:
        - To set your environment variables: source
    /opt/intel/inspector_xe_2013/inspxe-vars.sh
        - To start the graphical user interface: inspxe-gui
        - To use the command-line interface: inspxe-cl
        - For more getting started resources: /opt/intel/inspector_xe_2013/
          documentation/en/welcomepage/get_started.html.
    To get started using Intel(R) Advisor XE 2013 Update 2:
        - To set your environment variables: source
    /opt/intel/advisor_xe_2013/advixe-vars.sh
        - To start the graphical user interface: advixe-gui
        - To use the command-line interface: advixe-cl
        - For more getting started resources: /opt/intel/advisor_xe_2013/
          documentation/en/welcomepage/get_started.html.
    To get started using Intel(R) Composer XE 2013 Update 3 for Linux*:
        - Set the environment variables for a terminal window using one of the
          following (replace "intel64" with "ia32" if you are using a 32-bit
          platform).
          For csh/tcsh:
               $ source /opt/intel/bin/compilervars.csh intel64
          For bash:
               $ source /opt/intel/bin/compilervars.sh intel64
          To invoke the installed compilers:
               For C++: icpc
               For C: icc
               For Fortran: ifort

          To get help, append the -help option or precede with the man command.
        - For more getting started resources:
               /opt/intel/composer_xe_2013/Documentation/en_US/get_started_lc.htm.
               /opt/intel/composer_xe_2013/Documentation/en_US/get_started_lf.htm.

          
    To view movies and additional training, visit
    http://www.intel.com/software/products.

    --------------------------------------------------------------------------------
    q. Quit [default]
    --------------------------------------------------------------------------------
    Please type a selection or press "Enter" to accept default choice [q]: 

修改环境变量
============

在.bashrc中加入如下语句

.. code-block:: bash

 # Intel
 source /opt/intel/vtune_amplifier_xe_2013/amplxe-vars.sh
 source /opt/intel/inspector_xe_2013/inspxe-vars.sh
 source /opt/intel/advisor_xe_2013/advixe-vars.sh
 source /opt/intel/bin/compilervars.sh intel64

使环境变量生效：

.. code-block:: bash

 $ . .bashrc
 Copyright (C) 2009-2013 Intel Corporation. All rights reserved.
 Intel(R) VTune(TM) Amplifier XE 2013 (build 274450)
 Copyright (C) 2009-2013 Intel Corporation. All rights reserved.
 Intel(R) Inspector XE 2013 (build 278112)
 Copyright (C) 2009-2013 Intel Corporation. All rights reserved.
 Intel(R) Advisor XE 2013 (build 270011)

出来一堆版权说明好烦人，再改.bashrc如下：

.. code-block:: bash

 source /opt/intel/vtune_amplifier_xe_2013/amplxe-vars.sh quiet
 source /opt/intel/inspector_xe_2013/inspxe-vars.sh quiet
 source /opt/intel/advisor_xe_2013/advixe-vars.sh quiet
 source /opt/intel/bin/compilervars.sh intel64

搞定收工！

.. _`http://software.intel.com/en-us/non-commercial-software-development`: http://software.intel.com/en-us/non-commercial-software-development
