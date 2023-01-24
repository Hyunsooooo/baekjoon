N =int(input())
count = N
for i in range(N):
    word = str(input())
    my_list =[]
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            my_list.append(word[j])
        else:
            if word[j+1] in my_list:
                count-=1
                break
            else:
                my_list.append(word[j])
print(count)

