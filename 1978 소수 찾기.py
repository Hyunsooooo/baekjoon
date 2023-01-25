N= int(input())
my_list=list(map(int,input().split()))
max_value = max(my_list)
for i in range(2,max_value+1):
    for num in my_list:
        if (num%i==0) and (num != i):
            my_list.remove(num)
if 1 in my_list:
    my_list.remove(1)
print(len(my_list))