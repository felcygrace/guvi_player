l=int(input())
r=int(input())
count=0
for num in range(l,r+1):
    for i in range(2,num):
      if num%i==0:
        break
    else:
      count+=1
print(count)
