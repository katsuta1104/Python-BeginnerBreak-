import bisect
N=int(input())
A=list(map(int,input().split()))
V=int(input())
A.sort()

ans=bisect.bisect(A,V)
print(ans)
