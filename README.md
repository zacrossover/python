# Pagerank
##发展历史

##算法介绍
我们先来看下 PageRank 是如何计算的。
我假设一共有 4 个网页 A、B、C、D。它们之间的链接信息的有向图所图示：

![pagerank1](https://github.com/zacrossover/python/assets/15845563/06eada68-13c7-40eb-aa17-897085eaf355)


页面的Pagerank就等于所有入链的分数总和。我们假设每个页面的分数是平均分配给所有出链的，令所有页面的总分数都是1，为各边加权，可以得到下图：

![pagerank2](https://github.com/zacrossover/python/assets/15845563/5f9e4ecf-eb88-43bb-a192-11fadf0e7d67)



##时间复杂度分析

##代码实现

https://www.cnblogs.com/jpcflyer/p/11180263.html
https://mahua.jser.me/
