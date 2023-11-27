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

![image](https://github.com/zacrossover/python/assets/15845563/73ccd92a-76a6-4df9-8551-dabbadb16076)

之后我们假设四个网页初始的影响力相同，可以得到下面的向量

![image](https://github.com/zacrossover/python/assets/15845563/b90c33b2-7a0b-4abc-bb19-482eb8c4a966)

对初始影响力



## 时间复杂度分析

## 代码实现

https://www.cnblogs.com/jpcflyer/p/11180263.html
https://mahua.jser.me/
