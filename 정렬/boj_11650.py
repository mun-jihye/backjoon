## 리스트 안에 리스트를 인덱싱
import sys
input=sys.stdin.readline

test = int(input())

array=[]
for i in range(test):
    [x, y] = map(int, input().split())
    array.append([y, x])

s_array=sorted(array)

for i in range(test):
    print(s_array[i][1], s_array[i][0])