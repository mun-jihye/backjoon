word = input()
alphabet = list(range(97,123))  ##아스키코드 숫자 범위

for x in alphabet:
    print(word.find(chr(x)))

'''
find 함수는 어떤 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력한다. 
만일 찾는 문자가 문자열 안에 없는 경우에는 -1을 출력하는 함수이다. 


find 함수는 문자열에서만 사용 가능한 함수이다.
이와 유사한 기능을 하는 함수로 index 함수가 있다. 
index 함수는 문자열뿐만 아니라 리스트, 튜플과 같은 반복 가능한 iterable 자료형에서도 찾는 문자의 인덱스를 반환하는 함수로 쓰인다. 
find 함수와 다른 점은 find 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력하지만 index함수는 >AttributeError가 발생한다.
'''