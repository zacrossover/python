import time
import networkx as nx
import numpy as np
import random
import pandas as pd



df = pd.read_csv('data/222.csv')
edges = [edge for edge in zip(df['head'], df['tail'])]


G = nx.DiGraph()
G.add_edges_from(edges)

start_time = time.time()
pagerank1 = nx.pagerank(G,                     # NetworkX graph 有向图，如果是无向图则自动转为双向有向图
                       alpha=0.85,            # Damping Factor
                       personalization=None,  # 是否开启Personalized PageRank，随机传送至指定节点集合的概率更高或更低
                       max_iter=100,          # 最大迭代次数
                       tol=1e-06,             # 判定收敛的误差
                       nstart=None,           # 每个节点初始PageRank值
                       dangling=None,         # Dead End死胡同节点
                      )
end_time = time.time()

print("程序运行时间为：", end_time-start_time)


#print(pagerank1)

G_tmp = nx.read_edgelist('data/web-Google.txt', create_using = nx.DiGraph)

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