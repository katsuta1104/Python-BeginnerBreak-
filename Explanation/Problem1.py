A,B,C,S=map(int,input().split())
#A,B,C,Sを受け取る
ans=0

for i in range(1,A+1):
  for j in range(1,B+1):
    for k in range(1,C+1):
      if i+j+k==S:
        ans+=1
      #もし、i+j+kがSと等しいならansを1増やす

print(ans)
