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