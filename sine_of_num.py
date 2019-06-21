import math
n=int(input())
a=math.randians(n)
if a>0 and a<1:
  print(round(math.sin(a),2))
else:
  print(round(math.sin(a)))
