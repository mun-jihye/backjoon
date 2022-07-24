## 셀프넘버 n을 return 해주는 함수
def d(n):
    n = n + sum(map(int,str(n)))  ## str()은 ()안에 수를 str형으로 바꿔줌
    return n

## 셀프넘버가 아닌 수를 저장하는 집합 (생성자가 있는 수) : 중복제거
noself = set()

## 생성자를 골라 noself에 넣어준다.
for i in range(1,10001):
    noself.add(d(i))

## noself에 없는 수를 출력한다.
for j in range(1,10001) :
    if j not in noself:
        print(j)