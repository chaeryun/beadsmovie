### 'string' .replace(old, new , [])



문자열은 인덱스 할 수 있다. 순서가 있기 때문

String[0] = 'a'



.replace는 원본을 바꾸는게 아니라 바꾼값을 다른 변수에 저장하는것

list는 자체에 추가하는것이니까 원본을 바꾸는것



그 둘의 차이를 생각해보자

 pop() 제거됐던 부분이 무엇이엇는지 알수 있게 해주는 

### str.find(x) - x자체를 찾아서 걔 위치를 반환

x의 첫번째 위치를 반환. 없으면, -1을 반환함



### .index(x)

x의 첫번째 위치를 반환, 없으면 오류 발생



dict.get('x') 키값 x 찾아서 value 반환 - 없으면 오류

dict['x'] 키값 x 찾아서 value 반환 - 없으면 None 반환



error 발생했을때 다른문구 실행할 수 있는 거 try except



.replace(old, new[,count])

old에 넣을 값을 new로 바꿔주는 것



count 횟수만큼만 반복 시행 



.strip([chars])

특정한 문자들을 지정하면 제거하는것 

양쪽 제거 strip

왼쪽제거 lstrip

오른쪽 제거 rstrip



지정하지 않으면 공백을 제거함

## ★ .split([chars])

문자열을 특정한 단위로 나눠 리스트로 반환



문자열 자르기

s[::]  'abcdefghi'처음부터 끝까지 - 1 전체출력(스텝도 생략) 

s[::-1] 'ihgfedcba'



.find(x)

- x의 첫번째 위치를 반환. 없으면 -1을 반환
- 'apple'.find('p') #=>1
- 'apple'.find('k') # =>-1

index

- x의 첫번째 위치를 반환. 없으면 ValueError 일으킴
- 'apple'.find('p') #=>1
- 'apple'.find('k') # => ValueError



문자열 변경 

.replace(old, new[,count])

```python
'woooowoo'.replace('o','!',2) #o를 !로 바꾸는데 2개만 바꿔라
```



리스트

변경가능, 순서 있고 반복 가능

.extend(iterable) 항목이 들어간다. 



.insert(i, x)

정해진 위치 i에 값x를 추가함

map(function, iterable)

- 순회가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과를 map object로 반환



.add(elem)

.update(*others)

여러 값을 추가

