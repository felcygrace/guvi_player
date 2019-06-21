n=int(input())
l=[]
for i in range(n):
  i=int(input())
  l.append(i)
a=min(l)
l.remove(a)
b=min(l)
print(b)
