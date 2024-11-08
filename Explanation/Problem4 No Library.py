N=int(input())
A=list(map(int,input().split()))
V=int(input())
A.sort()
left=0
right=N-1
while left<=right:
    mid=(left+right)//2#真ん中を取る
    if A[mid] == V:
        print(mid+1)#1-indexedに戻す
        break
    if A[mid]<V:
        left=mid+1
    else:
        right=mid-1
