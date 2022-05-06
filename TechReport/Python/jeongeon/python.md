# Python

인터프리터 언어로 소스 코드를 컴파일 하지 않고, 한 줄씩 소스코드를 읽어서 바로 실행
컴파일 언어에 비해 느릴 수 있지만 빌드 과정이 없이 바로 실행 가능

## 주석

한 줄 주석은 #으로 표현
여려 줄 주석을 한 줄씩 #을 사용하거나 """ 또는 ''' 으로 표현
""" 또는 '''은 docstring을 위해 사용(함수/클래스의 설명)

## 코드라인

1줄에 1문장이 원칙
기본적으로 세미콜론(;)을 작성하지 않지만 한 줄로 표기할 때는 세미콜론(;)를 작성하여 표기가능
ex) print('hello);print('world)

## 데이터타입

### 숫자

모든 정수의 타입은 int 타입(Python 3 기준)
매우 큰 수를 나타낼 때 오버플로 발생 X

정수가 아닌 모든 실수는 float 타입
값 비교하는 과정에서 정수가 아닌 실수일 경우 주의할 것 (부동소수점에서 실수 연산 과정에서 error 발생 가능) -> math 모듈 활용

실수부와 허수부로 구성된 복소수는 모두 complex 타입
허수부를 j로 표현

### 문자열

모든 문자는 str 타입
문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하기 표기
문자열 내에서 특정 문자나 조작을 위해서 역슬래시(\)를 활용하여 구분

## 제어문

### 조건문

a, b = map(int, input("a와 b를 입력하세요: ").split(' '))
if a > b:
print(a\*b)
else:
print(b-a)

else if문은 elif로 표현

### 반복문

while과 for문이 있음
for 문은 유용하고 구조도 보기쉬운데, 여기서 같이 쓰이는 함수가 range 다

for i in [1,2,3]:
[]같은 iterable(반복가능한 객체)의 요소(1, 2, 3)를 처음부터 끝까지 i라는 변수로 뽑아내면서 for 문의 실행문을 반복한다.
여기서 리스트 요소를 간편하게 range()함수를 사용해서 나타낼 수 있다.

j = 0
while j <= 10:
print(j)
j += 1

while 문도 있는데, c언어 에서와 같다.
그리고 반목문과 조건문에서 쓰이는 예악어들도 있는데, break, continue 추가로 pass 도 있다.
break 는 가까운 반복문을 탈출 하고,
pass 와 continue 모두 아래 실행문을 무시하고 건너뛰는데, 이때 둘의 차이점은
pass 는 다음 루프를 실행시키지 않지만, continue 는 다음 루프로 넘어간다.

#### break 문

n = 0
while True:
n += 1
if n > 5:
print("break!")
break
print(n)

#### pass 문

pas = True
for i in range(1, 3):
if pas:
print("pass 전 i값: ", i) # -> 1
pas = False
pass
print("pass 후 i값: ", i) # -> 1
break

#### continue 값

con = True
for i in range(1, 3):
if con:
print("continue 전 i값: ", i) # -> 1
con = False
continue
print("continue 후 i값: ", i) # -> 2
break
