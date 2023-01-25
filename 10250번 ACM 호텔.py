import math
T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())
    if N%H == 0:
        a = H
    else:
        a= N%H
    b = math.ceil(N/H)
    print(a*100+b)