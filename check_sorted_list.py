n=int(input())
l=[]
c=0
for i in range(n):
  i=int(input())
  l.append(i)
if l==sorted(l):
  print('yes')
else:
  print('no')
