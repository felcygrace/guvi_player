n=[int(n) for n in input().split()]
k=[int(k) for k in input().split()]
s=[int(s) for s in input().split()]
if(n[0]*(k[1]-s[1])+k[0]*(n[1]-s[1])+s[0]*(n[1]-k[1])==0):
  print("yes")
else:
  print("no")
