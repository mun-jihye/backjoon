test = int(input())

for i in range(test):
    num, s = input().split()
    for x in s:
        print(x*int(num), end='')
    print()

