n=int(input())
k=int(input())
l=[]
c=0
for num in range(n):
  num=int(input())
  l.append(num)
for i in l:
  if k==i:
     c+=1
if c>0:
  print("yes")
else:
  print("no")
