# var = int(input())
# print(var) #  11 -> 11


#  1. input()의 반환값은 문자열이 기본
# var = input()
# print(var) # hello -> hello

#  실수형(float)로 받기
# var = float(input())
# print(var)

"""
2. 정수(int) 2개를 입력받아 그대로 출력해보자.(단, 띄어쓰기를 기준으로 입력한다.)
입력: 1 5
출력: 1 5
Tip::
    2.1 문자열의 메소드(함수) 인 split()을 이용하면 문자열을 공백 기준으로
       배열(iterable)을 만들어준다.
    2.2 매핑함수인 map()을 이용하면 배열(iterable)의 모든 원소를 첫 번째
       매개변수(parameter)로 변환할 수 있다. 정확히는 감싸준다는 표현이 맞다.
       예) map(int, ['1', '2', '3']) >> [1, 2, 3]
    3.3 매핑함수 map()의 반환값은 map 객체이다. 따라서 육안으로 확인하기
       위해서는 list()로 변환시켜 줘야 한다.
"""
# var = list(map(int, input().split(", ")))
# print(var[0], var[1])

"""
-list() 와 split()를 사용하지 않으면?-
list()로 변환해주지 않으면
TypeError: 'map' object is not subscriptable 
라고 에러가 뜬다.
split(",") 라고 입력하면 쉼표와 쉼표+띄어쓰기 까지 구분해준다.
split(", ") 은 무조건 쉼표 후 띄어쓰기가 포함되어야 에러가 안난다.
이를 어기면
ValueError: invalid literal for int() with base 10: '1,2'
가 뜬다.
"""

"""
3. 2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.
아스키 코드란?
    - 컴퓨터가 문자를 읽을 수 있도록 문자에 대응하는 숫자들이 존재한다.
    - 예) A => 1100001
    - 이때의 문자가 '아스키 문자'이며, 숫자가 '아스키 코드'이다.
"""
# var = input().split()
# print(var[1], var[0])
"""
Run:
a b
B a
"""

"""
4. 실수(float) 1개를 입력받아 저장한 후, 저장되어 있는 값을 소수점 셋 째 자리
에서 반올림하여 소수점 이하 둘 째 자리까지 출력하시오.
Tip::
    1. 반올림 함수 round()를 이용하면 된다.
"""
# var = round(float(input()), 2)
# print(var)
"""
3.144
3.14

3.145
3.15
"""

"""
5. 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.
-입력-
년, 월, 일이 ".(닷)"으로 구분되어 입력된다.
-출력-
입력받은 연,월,일을 yyyy.mm.dd 형식으로 출력한다.
입력:2020.2.9
출력:2020.02.09
(단, m 혹은 d가 한 자리 수인 경우 앞에 0을 붙여 출력한다.)
"""
# y, m, d = input().split('.')
# if len(m) == 1:
#     m = '0' + m
# if len(d) == 1:
#     d = '0' + d
# print('{}.{}.{}'.format(y, m, d))

"""
6. 주민번호는 다음과 같이 구성된다.

XXXXXX-XXXXXXX
앞의 6자리는 생년월일(yymmdd)이고 뒤 7자리는 성별, 지역, 오류 검출 코드이다.
주민번호를 입력받아 형태를 바꿔 출력해보자.
-입력-
주민번호 앞 6자리와 뒷7자리가 '-'로 구분되어 입력된다.(입력값은 가상의 주민번호이다.)ex)110011-0000000
-출력-
'-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.
입력:000907-1121112
출력:0009071121112
"""
# a, b = input().split('-')
# print('{}{}'.format(a, b))

"""
7. 1개의 문자열을 입력받아 그대로 출력해보자.
"""
# string = input()
# print(string)

"""
8. 공백이 포함되어 있는 한 문장이 입력된다. 단, 입력되는 문장은 여러 개의
단어로 구성되고, 엔터로 끝난다.
"""
# string = input()
# print(string)

"""
9. 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
-입력-
1.435867
-출력-
1
435867
"""
# string = input().split('.')
# print('''\
# {}
# {}
# '''.format(string[0], string[1]))

"""
10. 단어를 1개 입력 받는다.
입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력한다.
(단, 단어의 문자(영어)를 하나씩 나누어 한 줄에 한 개씩''로 묶어서 출력한다.)
입력:
'Boy'
출력:
'B'
'O'
'Y'
Tip::
    1. str도 List와 동일하게 배열과 같은 형식으로 접근 가능하다. 
       문자열도 리스트와 같이 iterable(반복가능한)객체 이기 때문이다.
       ex) '문자열'[0] -> '문'
    2. 반복문 for()를 이용하여 문자열의 길이만큼 반복한다.
"""
# string = input()
# for i in range(len(string)):
#     print("'{}'".format(string[i]))


"""
11. 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
-입력-
75254
-출력-
[70000]
[5000]
[200]
[50]
[4]
Tip::
    1. 문자열 연산이 가능함을 잊지 말자.
       ex) '문자' * 5 -> '문자문자문자문자문자'
"""
# integer = input()
# count = len(integer) - 1
# for i in range(len(integer)):
#     print([int(integer[i] + '0' * count)])
#     count -= 1

"""
12. 입력되는 시:분:초 에서 분만 출력해보자.
"""
# h, m, s = input().split(':')
# print(m)
"""
Run:
17:24:55
24
"""
"""
해설:
17:24:55 를 입력하면 split이 ':'을 기준으로 배열을 생성후 대입한다.
h, m, s = [17, 24, 55]와 같은 형태가 되고
print(m)을 하면 24가 m에 대입되었으니 24가 출력된다.
"""

"""
13. 년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.
년월일(yyyy.mm.dd)를 입력받아,
일월년(dd-mm-yyyy)로 출력해보자.
(단, 한 자리 일/월은 0을 붙여 두자리로 출력한다.)
Tip::
    1. 조건문 if-else문을 파이썬의 3항연산자 기능을 이용하면 간단하게 작성할 수 있다.
       메모리 효율성에도 효과적이다.
"""
y, m, d = input().split('.')
m = '0' + m if len(m) == 1 else m
d = '0' + d if len(d) == 1 else d
print('{}-{}-{}'.format(d, m, y))