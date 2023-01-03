test = int(input())
numbers = map(int, input().split())
cnt =0

def primenumber(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

for num in numbers:
    if num > 1:
        if primenumber(num) == True:
            cnt +=1
        else:
            continue
    else :
        continue

print(cnt)