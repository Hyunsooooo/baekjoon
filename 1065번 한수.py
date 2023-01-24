def solve(N):
    count=0
    for i in range(N):
        num = str(i+1)
        if len(num)==2:
            count+=1
        elif len(num) == 1:
            count+=1
        elif len(num) ==3:
            if int(num[0])+int(num[2]) == int(num[1])*2:
                count+=1
            else:
                pass
        else:
            pass
    return count

N=int(input())
print(solve(N))
        

