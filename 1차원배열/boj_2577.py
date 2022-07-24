a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))

for i in range(10):
    print(result.count(str(i)))  ##count : 그 리스트에 문자가 몇개 있는지 count