#함수를 이용해 계산기 프로그램은 만들어보자
#return 함수 4개가 주어진다 각각 +-*/
def Plus(x,y) :
    return x+y
def Minus(x,y) :
    return x-y
def Multiple(x,y) :
    return x*y
def Divide(x,y) :
    if x%y==0 :
        return x // y
    return x/y
print('--계산기 프로그램--')
num=0
con=0
while True :
    print('\n현재 숫자 :',num,'\n')
    print('1. 숫자 설정')
    print('2. 계산 설정')
    print('3. 종료')
    con=int(input('>>'))
    if con==3 :
        break;
    elif con==1 :
        num=int(input('숫자를 입력하시오'))
    elif con==2 :
        second=int(input('계산에 사용할 숫자를 입력해주세요!>>'))
        re=input('==더하기 / 빼기 / 곱하기 / 나누기==')
        if re=='더하기' or re=='+' :
            num=Plus(num,second)
        elif re=='빼기' or re=='-' :
            num=Minus(num,second)
        elif re=='곱하기' or re=='*' :
            num=Multiple(num,second)
        elif re=='나누기' or re=='/' :
            num=Divide(num,second)
        else :
            print('잘못된 선택입니다.')

        print('결과 :',num)
    else :
        print('잘못된 선택입니다.')

print('--계산기 사용 종료--')
