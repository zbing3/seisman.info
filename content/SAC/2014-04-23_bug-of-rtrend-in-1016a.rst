SAC 101.6a中rtrend的一个Bug
###########################

:date: 2014-04-23 14:00
:author: SeisMan
:category: SAC
:tags: bug
:slug: bug-of-rtrend-in-1016a

SAC 101.6中对rtrend的源码进行了修改，引入了一个新的bug，并进一步影响到了101.6a版本。

在对等间隔时间数据使用rtrend命令时，会调用子函数\ ``lifite``\ 计算数据的最小二乘线性拟合。源码位于\ ``sac/src/scm/lifite.c``\ 中，错误的部分如下：

.. code-block:: c

    xi = x1;                                                                        
    for( i = 1; i <= n; i++ ){                                                      
        yi = Y[i];                                                                  
        xi = x1 + (dx * i-1); 
        sumx = sumx + xi;                                                           
        sumy = sumy + Y[i];                                                         
        sumxy = sumxy + xi*yi;                                                      
        sumx2 = sumx2 + xi*xi;                                                      
        sumy2 = sumy2 + yi*yi;                                                      
    }                                                                            
    
正确的代码应为：

.. code-block:: c

    xi = x1;                                                                        
    for( i = 1; i <= n; i++ ){                                                      
        yi = Y[i];                                                                  
        xi = x1 + (dx * (i-1)); // 少了一对括号
        sumx = sumx + xi;                                                           
        sumy = sumy + Y[i];                                                         
        sumxy = sumxy + xi*yi;                                                      
        sumx2 = sumx2 + xi*xi;                                                      
        sumy2 = sumy2 + yi*yi;                                                      
    }                                                                            

这个Bug导致，当采样间隔dx不为1的情况下，线性拟合得到的截距出现错误，但不影响斜率。最终在被rtrend调用时，生成的波形数据中线性趋势被正确去除，但其均值不为0，这可能会影响到后续数据处理的正确性。
