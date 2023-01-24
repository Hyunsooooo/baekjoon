N =int(input())
count = 0
for i in range(N):
    word = str(input())
    for j in range(len(word)):
        my_list=[]
        if word[j] == word[j+1]:
            my_list.append(word[j])
            
        else:
