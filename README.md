# Pagerank
## 发展历史

PageRank，又称网页排名、谷歌左侧排名、PR，是Google公司所使用的对其搜索引擎搜索结果中的网页进行排名的一种算法。佩奇排名本质上是一种以网页之间的超链接个数和质量作为主要因素粗略地分析网页的重要性的算法。其基本假设是：更重要的页面往往更多地被其他页面引用（或称其他页面中会更多地加入通向该页面的超链接）。 其将从A页面到B页面的链接解释为“A页面给B页面投票”，并根据投票来源（甚至来源的来源，即链接到A页面的页面）和投票对象的等级来决定被投票页面的等级。该算法以谷歌公司创始人之一的拉里·佩奇（Larry Page）的名字来命名。谷歌搜索引擎用它来分析网页的相关性和重要性，在搜索引擎优化中经常被用来作为评估网页优化的成效因素之一。

目前，佩奇排名算法不再是谷歌公司用来给网页进行排名的唯一算法，但它是最早的，也是最著名的算法。

## 算法介绍
我们先来看下 PageRank 是如何计算的。
一个网页的pagerank是网页的重要程度。引用可以看成是其他网页对该网页的投票，更重要的网页引用比不重要的网页引用权重更高，计算该网页的pagerank需要引用网页的pagerank，计算引用网页的pagerank又要先计算引用他的网页的pagerank，所以该问题是一个递归问题。

我假设一共有 4 个网页 A、B、C、D。它们之间的链接信息的有向图所图示：

![pagerank1](https://github.com/zacrossover/python/assets/15845563/06eada68-13c7-40eb-aa17-897085eaf355)

Pagerank值的公式如下所示：

$$ PR(p_i) = \sum_{p_j \in M(p_i)} \frac{PR(p_j)}{L(p_j)} $$ 

页面的Pagerank就等于所有入链的分数总和。我们假设每个页面的分数是平均分配给所有出链的，令所有页面的总分数都是1，为各边加权，可以得到下图：

![pagerank](https://github.com/zacrossover/python/assets/15845563/9af78cc6-ad93-49be-850f-311fb3b194f2)


根据上述加权有向图可以生成一个转移矩阵M，元素的值代表从一个页面到另一个页面的投票

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

根据上面算法分析，该算法的运行过程为不断算 $n \times n$ 矩阵乘以一个n维向量，单次做矩阵乘法的时间复杂度为n^2，令迭代次数为 $t(\varepsilon)$ ，则时间复杂度为：

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

查看函数源代码，逻辑为幂迭代，不断左乘转移矩阵，在差值小于tol时返回。
```python
    import numpy as np
    import scipy as sp

    N = len(G)
    if N == 0:
        return {}

    nodelist = list(G)
    A = nx.to_scipy_sparse_array(G, nodelist=nodelist, weight=weight, dtype=float)
    S = A.sum(axis=1)
    S[S != 0] = 1.0 / S[S != 0]
    # TODO: csr_array
    Q = sp.sparse.csr_array(sp.sparse.spdiags(S.T, 0, *A.shape))
    A = Q @ A

    # initial vector
    if nstart is None:
        x = np.repeat(1.0 / N, N)
    else:
        x = np.array([nstart.get(n, 0) for n in nodelist], dtype=float)
        x /= x.sum()

    # Personalization vector
    if personalization is None:
        p = np.repeat(1.0 / N, N)
    else:
        p = np.array([personalization.get(n, 0) for n in nodelist], dtype=float)
        if p.sum() == 0:
            raise ZeroDivisionError
        p /= p.sum()
    # Dangling nodes
    if dangling is None:
        dangling_weights = p
    else:
        # Convert the dangling dictionary into an array in nodelist order
        dangling_weights = np.array([dangling.get(n, 0) for n in nodelist], dtype=float)
        dangling_weights /= dangling_weights.sum()
    is_dangling = np.where(S == 0)[0]

    # power iteration: make up to max_iter iterations
    for _ in range(max_iter):
        xlast = x
        x = alpha * (x @ A + sum(x[is_dangling]) * dangling_weights) + (1 - alpha) * p
        # check convergence, l1 norm
        err = np.absolute(x - xlast).sum()
        if err < N * tol:
            return dict(zip(nodelist, map(float, x)))
    raise nx.PowerIterationFailedConvergence(max_iter)
```


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
pagerank2 = nx.pagerank(G_tmp,                
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

## 分布式研究
真的的web结构的转移矩阵非常大，目前的网页数量已经超过100亿，转移矩阵是100亿*100亿的矩阵，直接按矩阵乘法的计算方法不可行，需要借助Map-Reduce的计算方式来解决。实际上，google发明Map-Reduce最初就是为了分布式计算大规模网页的pagerank。map的过程其实就是对矩阵乘法的机损过程进行拆分，reduce过程就是将指向各个节点的权重进行加总，然后用一次mapreduce的结果作为下一次mapreduce的输入数据，迭代计算。


## 算法缺陷


PageRank算法的主要缺点在于旧的页面的排名往往会比新页面高。因为即使是质量很高的新页面也往往不会有很多外链，除非它是某个已经存在站点的子站点。这也是PageRank需要多项算法结合以保证其结果的准确性的原因。例如，PageRank似乎偏好于维基百科页面，在条目名称的搜索结果中，维基百科页面经常在大多数页面甚至所有页面之前，此现象的原因则是维基百科内部网页中存在大量的内链，同时亦有很多站点链入维基百科。


## 参考资料

https://www.cnblogs.com/jpcflyer/p/11180263.html

https://zh.wikipedia.org/wiki/PageRank

https://www.cnblogs.com/fengfenggirl/p/pagerank-introduction.html


