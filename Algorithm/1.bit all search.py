N=int(input())
X=int(input())
A=list(map(int,input().split()))

for i in range(2**N):
    sum_value=0
    for j in range(N):
        if (i>>j)&1:#もしj番目のビットが1なら
            sum_value+=A[j]
    
    if sum_value==X:
        print("Yes")
        exit()

print("No")
