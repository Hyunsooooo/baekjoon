my_dict = {1:[],2:['A','B','C'],
                   3:['D','E','F'],
                      4:['G','H','I'],
                         5:['J','K','L'],
                            6:['M','N','O'],
                               7:['P','Q','R','S'],
                                  8:['T','U','V'],
                                     9:['W','X','Y','Z']}
N = str(input())
my_list=[]
for i in list(N):
    my_list.append(sum([x+1 for x in range(1,10) if i in my_dict[x]]))

print(sum(my_list))