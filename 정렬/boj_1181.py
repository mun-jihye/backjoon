
test = int(input())
a=[]

for i in range(0,test):
    a.append(input())

## 중복 제거
a = list(set(a))   ## 집합 함수 set  ((순서가 없고 중복 제거 가능  --> 다시 리스트로 전환

## 정렬렬
a.sort()  ## 아무값도 넣지 안흥면 알파벳 순서대로 정렬해준다.
a.sort(key=len)  ## 문자열 길이 순으로 정렬

for i in a:
    print(i)