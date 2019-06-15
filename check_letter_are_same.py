a=input()
b=input()
k=int(input())
c=0
for i in range(len(a)):
  if a[i]!=b[i]:
    c+=1
if c==k:
  print("yes")
else:
  print("no")
