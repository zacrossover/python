# Pagerank
## 发展历史

PageRank，又称网页排名、谷歌左侧排名、PR，是Google公司所使用的对其搜索引擎搜索结果中的网页进行排名的一种算法。佩奇排名本质上是一种以网页之间的超链接个数和质量作为主要因素粗略地分析网页的重要性的算法。其基本假设是：更重要的页面往往更多地被其他页面引用（或称其他页面中会更多地加入通向该页面的超链接）。 其将从A页面到B页面的链接解释为“A页面给B页面投票”，并根据投票来源（甚至来源的来源，即链接到A页面的页面）和投票对象的等级来决定被投票页面的等级。该算法以谷歌公司创始人之一的拉里·佩奇（Larry Page）的名字来命名。谷歌搜索引擎用它来分析网页的相关性和重要性，在搜索引擎优化中经常被用来作为评估网页优化的成效因素之一。

目前，佩奇排名算法不再是谷歌公司用来给网页进行排名的唯一算法，但它是最早的，也是最著名的算法。

## 算法介绍
我们先来看下 PageRank 是如何计算的。
一个网页的pagerank是网页的重要程度，可以看成是其他网页对该网页的投票，更重要的网页引用比不重要的网页引用权重更高，计算一个网页的pagerank又要先计算引用他的网页的pagerank，所以该问题是一个递归问题。

我假设一共有 4 个网页 A、B、C、D。它们之间的链接信息的有向图所图示：

![pagerank1](https://github.com/zacrossover/python/assets/15845563/06eada68-13c7-40eb-aa17-897085eaf355)

Pagerank值的公式如下所示：

$$ PR(p_i) = \sum_{p_j \in M(p_i)} \frac{PR(p_j)}{L(p_j)} $$ 

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

上面过程相当于不断的对初始向量w_0做左乘矩阵M的操作，当上一次的结果w_i于w_i+1的差小于一个 $\epsilon$ 时，迭代结束，得到的向量w_i+1即为最终的pagerank值，改方法叫幂迭代。

但在现实情况中，可能存在某些页面没有向外的链接，那经过迭代之后，这个页面的pagerank将变为1，其他页面都为0；或者某些页面没有访问它的页面，那它的pagerank将是0，这些结果都是没有意义的。为了解决这个问题，该算法引入了随机浏览者（random surfer）的概念，即假设某人在浏览器中随机打开某些页面并点击了某些链接。为了便于理解，这里假设上网者不断点击网页上的链接直到进入一个没有外部链接的网页，此时他会随机浏览其他的网页（可以与之前的网页无关）。为了表达这种概率，引入一个阻尼系数d，表示用户与1-d的概率停止继续点击链接，随机浏览网页，pagerank的公式就变为 

$$ PR(p_i) = \frac{1-d}{N} + d \sum_{p_j \in M(p_i)} \frac{PR(p_j)}{L(p_j)} $$ 



## 时间复杂度分析

根据上面算法分析，该算法的运行过程为不断算 $ n \times n $ 矩阵乘以一个n维向量，单次做矩阵乘法的时间复杂度为n^2，令迭代次数为 $t(\varepsilon)$ ，则时间复杂度为：

$$ O(t(\varepsilon)n^2) $$


## 代码实现

代码实现方面，使用python的图数据挖掘包networkx。networkx可以以标准化和非标准化的数据格式存储网络、生成多种随机网络和经典网络、分析网络结构、建立网络模型、设计新的网络算法、进行网络绘制等。其中实现了Pagerank相关算法，可直接调用。

```python
pagerank1 = nx.pagerank(G,
                       alpha=0.85,            # Damping Factor
                       personalization=None,  # 是否开启Personalized PageRank，随机传送至指定节点集合的概率更高或更低
                       max_iter=100,          # 最大迭代次数
                       tol=1e-06,             # 判定收敛的误差
                       nstart=None,           # 每个节点初始PageRank值
                       dangling=None,         # Dead End死胡同节点
                      )
```

其中alpha参数代表阻尼系数，这里取0.85，最大迭代次数取100，收敛的误差 $\epsilon$ 取 $10^{-6}$ 。

代码执行过程中取两个数据集，小的数据集为三国演义的人物关系(data/三国演义/triples.csv)，该图包括123个节点和144条边；大数据集是2002年谷歌编程大赛的一个有向图数据集（/data/web_Google.txt），包括875713个节点和5105039条边。这两个数据集均在data文件夹下。分别对其读取，生成有向图，调用函数，排序，并按顺序输出pagerank最大的若干个节点，代码如下：
```python
df = pd.read_csv('data/三国演义/triples.csv')
edges = [edge for edge in zip(df['head'], df['tail'])]

G = nx.DiGraph()
G.add_edges_from(edges)

start_time = time.time()
pagerank1 = nx.pagerank(G,
                       alpha=0.85,            # Damping Factor
                       personalization=None,  # 是否开启Personalized PageRank，随机传送至指定节点集合的概率更高或更低
                       max_iter=100,          # 最大迭代次数
                       tol=1e-06,             # 判定收敛的误差
                       nstart=None,           # 每个节点初始PageRank值
                       dangling=None,         # Dead End死胡同节点
                      )
end_time = time.time()

print("程序运行时间为：", end_time-start_time)
sorted1 = sorted(pagerank1.items(),key=lambda x : x[1], reverse=True)
print(sorted1)

G_tmp = nx.read_edgelist('data/web-Google.txt', create_using = nx.DiGraph)
print(len(G_tmp))
start_time2 = time.time()
pagerank2 = nx.pagerank(G_tmp,                     # NetworkX graph 有向图，如果是无向图则自动转为双向有向图
                       alpha=0.85,            # Damping Factor
                       personalization=None,  # 是否开启Personalized PageRank，随机传送至指定节点集合的概率更高或更低
                       max_iter=100,          # 最大迭代次数
                       tol=1e-06,             # 判定收敛的误差
                       nstart=None,           # 每个节点初始PageRank值
                       dangling=None,         # Dead End死胡同节点
                      )
end_time2 = time.time()
print("程序运行时间为：", end_time2-start_time2)

sorted2 = sorted(pagerank2.items(),key=lambda x : x[1], reverse=True)
top10 = sorted2[:10]
print(top10)
```

输出的截图如下：

![image](https://github.com/zacrossover/python/assets/15845563/7b7d4115-c492-4c4a-9ffc-1e8f1cb41cc1)

可以看到大数据集执行花费12.8秒，而小数据集花费0.6秒。小数据集中，诸葛亮的pagerank值最高，符合常识；大数据集中，163075号节点pagerank值最高，说明该节点最为重要。


## 算法缺陷


PageRank算法的主要缺点在于旧的页面的排名往往会比新页面高。因为即使是质量很高的新页面也往往不会有很多外链，除非它是某个已经存在站点的子站点。这也是PageRank需要多项算法结合以保证其结果的准确性的原因。例如，PageRank似乎偏好于维基百科页面，在条目名称的搜索结果中，维基百科页面经常在大多数页面甚至所有页面之前，此现象的原因则是维基百科内部网页中存在大量的内链，同时亦有很多站点链入维基百科。


## 引用

https://www.cnblogs.com/jpcflyer/p/11180263.html

https://zh.wikipedia.org/wiki/PageRank

