n = int(input())

def d(n):
    cnt = 0

    for i in range(1, n+1):
        num = list(map(int,str(i)))
        if i <= 99:  ## 두자리밖에 안되므로 공차가 일정한 지 알 수 없으므로 99보다 작은 수는 모두 한수
            cnt +=1
        elif num[0] - num[1] == num[1] - num[2]:
            cnt +=1
    return cnt

print(d(n))