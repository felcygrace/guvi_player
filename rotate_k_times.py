n=input()
k=int(input())
a=n
for i in range(0,k):
  a=a[-1]+a[:len(n)-1]
print(a)
