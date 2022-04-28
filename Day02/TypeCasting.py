#타입 캐스팅(type casting)
#사용하고 있는 값의 타입을 변경하는 기능

#사용 방법 : 변환하고자 하는 앞에 타입()으로 덮어주는 방식으로 사용한다.

print(str(10))
print(10)
#위의 두 코드로는 구분이 어렵다.

a=str(10)
b=10

print(a)
print(b)
print(type(a)) # <class 'str'>
print(type(b)) # <class 'int'>

#입력은 기본적으로 String 타입으로 저장된다.
number=input('숫자를 입력해주세요 >>')

#입력받은 number를 int타입으로 형변환
number=int(number)
print(number)


#입력과 동시에 형태를 지정
number2= int(input('숫자를 입력해주세요 >>'))
print(number2)
print(type(number2))


