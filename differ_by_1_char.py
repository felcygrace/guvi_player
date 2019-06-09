a=input()
b=input()
s=sum(a[i]!=b[i] for i in range(len(a)))
if s==1:
  print("yes")
else:
  print("no")
