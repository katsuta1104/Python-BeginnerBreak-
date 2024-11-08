N,K=map(int,input().split())
A=list(map(int,input().split()))

l=0
r=int(1e9)#1000000000

while l+1<r:
    mid=(l+r)//2
    num=0
    for a in A:
        num+=mid//a#mid秒で何枚刷れるか
    
    if num>=K:#刷れた枚数がK枚より以上なら右側の範囲を縮小
        r=mid
    else:
        l=mid#刷れた枚数がK枚よりも少ないなら左側の範囲を縮小
print(r)
