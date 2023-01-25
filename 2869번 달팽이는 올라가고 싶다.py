import math
A,B,V = map(int,input().split())
i = 1
V = V-A
i+=math.ceil(V/(A-B))
print(i)
