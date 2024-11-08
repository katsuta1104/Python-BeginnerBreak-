A,B,C,S=map(int,input().split())
ans=0

for i in range(1,A+1):
    for j in range(1,B+1):
        k=S-i-j
        #Sと等しいようなkはS-i-jしかない
        if i+j+k==S and 1<=k<=C:
            ans+=1
            #ここで、kはC以下の自然数であることに注意

print(ans)
