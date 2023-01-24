my_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
n = str(input())

for i in my_list:
    n=n.replace(i,'a')

print(len(n))