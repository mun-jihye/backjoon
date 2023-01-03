test = int(input())
list = []

for i in range(test):
    age, name = map(str, input().split())
    age = int(age)
    list.append((age, name))

list.sort(key = lambda x:x[0])  ## age만 비교하면 됨. 이미 가입순으로 정렬되어 있기 때문

for i in list:
    print(i[0], i[1])

