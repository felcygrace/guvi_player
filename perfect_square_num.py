l=int(input())
r=int(input())
c=0
li=[]
for i in range(1,r+1):
  sq=i*i
  if sq<=r:
     li.append(sq)
for j in range(l,r+1):
  if j in li:
    c+=1
print(c)
