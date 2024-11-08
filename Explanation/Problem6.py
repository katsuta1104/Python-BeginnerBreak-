N=int(input())
P=list(map(int,input().split()))

G=[[]for _ in range(N)]

#有向グラフの矢印の向きを逆転させる
for i in range(N-1):
    G[P[i]].append(i+1)

#DFSお実装する。ansを用いて部分木の頂点数を求める
def dfs(pos,visited,ans):
    if pos not in visited:
        visited.add(pos)
        ans[0]+=1
        for t in G[pos]:
            dfs(t,visited,ans)
    return ans[0]

#各頂点からの部分木に含まれる頂点数を求める
for i in range(N):
    ans=[0]
    visited=set()
    print(dfs(i,visited,ans))
