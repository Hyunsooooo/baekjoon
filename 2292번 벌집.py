N = int(input())
num =1
i=0
while num < N:
    num += i*6
    i +=1
if N == 1:
    print(1)
else:
    print(i)