M = int(input())
N = int(input())

my_list = list(range(M,N+1))
for i in range(2,N+1):
    for num in my_list:
        if (num%i==0) and (num != i):
            my_list.remove(num)
if 1 in my_list:
    my_list.remove(1)

if len(my_list)==0:
    print(-1)
else:
    print(sum(my_list))
    print(min(my_list))

