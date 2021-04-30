n=int(input())
ans=[]
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        ans.append(i)
        ans.append(n//i)
res=[]
for i in ans:
    for j in ans:
        for k in ans:
            if i*j*k==n:
                res.append((i,j,k))
print(len(res))
