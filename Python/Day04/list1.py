#자료구조 리스트 1

# 리스트 생성
'''
선형 자료구조(Linear Data Structure)

인덱스 : 묶여있는 값에서 하나의 값을 얻기 위한 숫자형 데이터(색인)
요소 : 자료구조 안에 들어있는 값

(1) 리스트의 형태로 만들기
변수명 = [요소1,요소2,요소3]
'''
numbers=[1,2,3,4,5,6,7,8,9,10]
numbers2=[] # 리스트에 요소값을 적지 않을 경우 빈 리스트가 만들어진다.

#1.2 list()를 통해서 리스트 형태로 만들기
numbers3=list(range(1,11))
#1.3 리스트 컴프리헨션(list comprehension)으로 리스트 만들기
#리스트명 = [변수 for문 if문 ...]
numbers4 = [number for number in range(1,11) if number%3==0]
#원하는 조건의 값을 바로 추가하기 때문에 많이 활용됨

#(2) 리스트를 통해 작업할 수 있는 기본적인 것들
for i in numbers :
    print(i,end=' ')

data = int(input('숫자를 입력해주세요>>'))
if data in numbers :
    print('해당 숫자는 이미 존재합니다.')
else :
    print(data)

if data:
    print(data)
else :
    print('data 안에 값이 없습니다.')
#조건문에 자료구조를 넣으면 값이 비어있는지 아닌지 확인 가능
# 1~100 3,5의 배수 만족값 리스트로 표현 조건 : 리스트 컴프리헨션
