n=int(input())
k=int(input())
a=max(n,k)
l=[]
for i in range(1,a+1):
  if(n%i==0 and k%i==0):
       l.append(i)
print(max(l))
