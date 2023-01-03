num = int(input())
li = list(map(int,str(num)))

list.sort(revere=True)  ## 내림차순

for i in list:
    print(i, end='')