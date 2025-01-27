N=int(input())
A=list(map(int,input().split()))
X=int(input())
ans=0

for i in range(2**N):
    sum_value=0
    for j in range(N):
        if (i>>j)&1:
            sum_value+=A[j]
    
    if sum_value==X:
        ans+=1
print(ans)
