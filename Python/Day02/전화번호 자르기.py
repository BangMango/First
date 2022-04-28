#이름과 전화번호를 입력받아 출력 진행하는 프로그램코드 작성

name=(input('이름을 입력하시오  '))
num=(input('-를 뺀 부분의 전화번호를 입력하시오  '))
# if 조건문

# if 조건식 :
#   명령문

# 조건문이 충족되지 않으면 오류가 난다.

if len(num) == 11 :
    first=num[0:3]
    #first의 경우 0으로 시작하게 된다면 사라지게된다.
    second=int(num[3:7])
    third=int(num[7:])
    #print()안에 ,를 넣을 경우 여러 문장을 표현할 수 있다.
    print('\n')
    print(first,second,third, sep='-')


    
'''
print()의 기능

1. ,를 사용할 경우 여러 변수 포함하여 출력
2. sep을 수정할 경우 ,기능 사용할 때 진행할 작업(띄어쓰기)을  변경한다.
3. end를 수정할 경우, print의 작업이 끝난 뒤의 작업을 변경한다.(줄띄기)
4. file의 경우 출력 관련 설정을 진행할 수 있다.특별한 경우가 아니라면 건드리지 않는다.
5. flush의 경우 버퍼링 여부를 처리한다.
(일반적으로 false상태 유지, true로 변경하면 버퍼 값을 바로 전달한다.)

'''




# len(변수) : 해당 변수의 크기(길이)를 반환한다.

'''

#인덱스(index) / 슬라이싱(slicing)

#인덱스 : 묶음의 형태로 저장되어있는 값 중 하나를 가리키는 숫자
apple='apple'
print(apple[2])

#슬라이싱 : 인덱스의 묶음
print(apple[0:3])

#슬라이싱의 뒤의 위치는 설정한 시작점과 무관하게 문장 길이에서 몇번째인지 작성
sentence='Hello, Monday!'
hello=sentence[0:5]
monday=sentence[7:13]
print(hello)
print(monday)

#파이썬은 인덱스의 음수번호를 제공한다.
#index -1은 문장의 마지막 값이 된다.
'''

#<출력결과>
'''
아이디로 사용할 문장을 입력해주세요. 최대 글자는 6글자까지 가능합니다 >>>
다음 주소 중 하나를 선택해주세요.
1. naver 2. gmail 3. kakao

'''
address=''
ID=input('아이디로 사용할 문장을 입력해주세요. 최대 글자는 6글자까지 가능합니다.')
if len(ID) > 6 :
    print('아이디가 6글자를 초과했습니다.')
else: 
    select=int(input('다음 주소 중 하나를 선택해주세요. \n 1.네이버 2.지메일 3.페이스북 4.다음'))
    if select==1 :
        address='naver.com'
    if select==2 :
        address='gmail.com'
    if select==3 :
        address='facebook.com'
    if select==4 :
        address='hanmail.com'
        
    print('ID가 생성되었습니다.')
    print(ID,address,sep='@')











