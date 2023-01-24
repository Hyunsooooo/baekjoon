N=input()

num = list(N.split('-'))


num

value = 0
if num[0] == '':
    value -= sum(map(int,num[1].split('+')))
    for i in range(2,len(num)):
        value -= sum(map(int,num[i].split('+')))

else:
    value += sum(map(int,num[0].split('+')))

    for i in range(1,len(num)):
        value -= sum(map(int,num[i].split('+')))

print(value)