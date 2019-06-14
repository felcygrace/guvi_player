n=int(input())
k=int(input())
l1=[]
l2=[]
for num in range(n):
  num=int(input())
  l1.append(num)
for numb in range(k):
  numb=int(input())
  l2.append(numb)
for i in l2:
  l1.append(i)
print(max(l1))
print(max(l2))
a=l1+l2
print(max(a))
