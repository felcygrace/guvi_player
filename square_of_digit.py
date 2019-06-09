n=int(input())
sum1=0
while n>0:
  s=n%10
  sum1=sum1+(s*s)
  n=n//10
print(sum1)

