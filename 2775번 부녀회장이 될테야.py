T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    my_list=[(list(range(1,n+1)))]
    for floor in range(0,1+k):
        loch_list=[]
        for loch in range(0,n):
            loch_list.append(sum(my_list[floor][0:loch+1]))
        my_list.append(loch_list)


    print(my_list[k][n-1])
        
