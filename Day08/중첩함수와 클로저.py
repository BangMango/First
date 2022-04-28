#중첩함수와 클로저

#중첩함수는 함수 내부에 또 다른 함수가 만들어져 있는 형태를 뜻한다.

#함수 안에서 반복되는 코드를 함수로 만들어 코드 관리의 가독성을 높인다.
'''
중첩 함수의 형태
def Outer() :
    명령문
    def Inner() :
        명령문
'''
data=''
def Test(d) :
    data=d
    
    def print_data() :
        print(data)
    def set_data(d) :
        data=d
        return data
    print_data()
    return print_data,set_data#클로저
#return 값이 2개 이상일 경우 튜플의 형태로 내보내진다.

a,b=Test("data")
#a에 print_data가 b에 set_data의 형태가 넘어간다.
a()
b('Data')


def Outer() :
    data=0
    def Inner() :
        nonlocal data
        data=1
        return  data
    Inner()
    return data
print(Outer())



#변수 영역 파악
global_variable="전역 변수"
def Function_Outer():
    nonlocal_variable="비전역 변수"
    print(global_variable)
    print(nonlocal_variable)
    def Function_Inner() :
        local_variable="지역 변수"
        print(global_variable)
        print(nonlocal_variable)
        print(local_variable)

    #print(local_variable) Inner에서 만든 값 사용 불가
print(global_variable) #전역 변수 사용 가능
print(nonlocal_variable)#outer 값 사용 불가
print(local_variable)#Inner 값 사용 불가
