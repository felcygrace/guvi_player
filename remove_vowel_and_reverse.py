a=input()
vowels=('a','e','i','o','u')
for i in a:
  for i in vowels:
    a=a.replace(i,'')
    b=a[::-1]
print(b)
