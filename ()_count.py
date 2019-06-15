a=input()
d=p=0
for i in a:
  if i=='(':
    d+=1
  if i==')':
    p+=1
if d==p:
  print("yes")
else:
  print("no")
