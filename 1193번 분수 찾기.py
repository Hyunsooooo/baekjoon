X = int(input())
N=0
num=0
for i in range(1,X+1):
    N=i
    if X <= (N*(N+1))/2:
        num=i
        break
    else:
        pass

level = int(X - num*(num-1)/2)
if num%2==0:

    print(str(level)+'/'+str(num-level+1))
else:
    print(str(num-level+1)+'/'+str(level))
