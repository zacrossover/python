# Pagerank
## 发展历史

## 算法介绍
我们先来看下 PageRank 是如何计算的。
一个网页的pagerank是网页的重要程度，可以看成是其他网页对该网页的投票，更重要的网页引用比不重要的网页引用权重更高，计算一个网页的pagerank又要先计算引用他的网页的pagerank，所以该问题是一个递归问题。

我假设一共有 4 个网页 A、B、C、D。它们之间的链接信息的有向图所图示：

![pagerank1](https://github.com/zacrossover/python/assets/15845563/06eada68-13c7-40eb-aa17-897085eaf355)


页面的Pagerank就等于所有入链的分数总和。我们假设每个页面的分数是平均分配给所有出链的，令所有页面的总分数都是1，为各边加权，可以得到下图：

![pagerank2](https://github.com/zacrossover/python/assets/15845563/5f9e4ecf-eb88-43bb-a192-11fadf0e7d67)

根据上述加权有向图可以转成一个矩阵，元素的值代表从一个页面到另一个页面的投票

$$M=
\begin{bmatrix}
0 & 1/2 & 1 & 0 \\
1/3 & 0 & 0 & 1/2 \\
1/3 & 0 & 0 & 1/2 \\
1/3 & 1/2 & 0 & 0 
\end{bmatrix}
$$


之后我们假设四个网页初始的pagerank相同，可以得到下面的向量w_0

$$w_0=
\begin{bmatrix}
1/4 \\
1/4 \\
1/4 \\
1/4
\end{bmatrix}
$$

对初始的pagerank进行第一次迭代，相当于对上面向量根据投票的矩阵进行线性变换，可以得到w_1

$$w_1 = Mw_0 = \left[
 \begin{matrix}
0 & 1/2 & 1 & 0 \\
1/3 & 0 & 0 & 1/2 \\
1/3 & 0 & 0 & 1/2 \\
1/3 & 1/2 & 0 & 0 
  \end{matrix}
  \right] \left[
 \begin{matrix}
1/4 \\
1/4 \\
1/4 \\
1/4
  \end{matrix}
  \right] =  \begin{bmatrix}
3/8 \\
5/24 \\
5/24 \\
5/24
  \end{bmatrix}$$


再对w_1进行投票，得到w_2:

$$w_2 = Mw_1 = \left[
 \begin{matrix}
0 & 1/2 & 1 & 0 \\
1/3 & 0 & 0 & 1/2 \\
1/3 & 0 & 0 & 1/2 \\
1/3 & 1/2 & 0 & 0 
  \end{matrix}
  \right] \left[
 \begin{matrix}
3/8 \\
5/24 \\
5/24 \\
5/24
  \end{matrix}
  \right] =  \begin{bmatrix}
5/16 \\
11/48 \\
11/48 \\
11/48
  \end{bmatrix}$$
  
依此类推，网页的pagerank向量w将最终收敛，这就是最后pagerank的结果。

$$\begin{bmatrix}
0.3333 \\
0.2222 \\
0.2222 \\
0.2222
  \end{bmatrix}$$

上面过程相当于不断的对初始向量w_0做左乘矩阵M的操作，当上一次的结果w_i于w_i+1的差小于一个无穷小值时，迭代结束，得到的向量w_i+1即为最终的pagerank值。



## 时间复杂度分析

## 代码实现

https://www.cnblogs.com/jpcflyer/p/11180263.html
https://mahua.jser.me/
