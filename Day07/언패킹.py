def Info (user) :
    print(user.get('name'))
    print(user.get('age'))
    print(user.get('address'))
'''
def Info(name,age,address) :
    print(f'이름 : {name}')
    print(f'나이 : {age}')
    print(f'주소 : {address}')
'''
def Info2(**args) :
    print(args)

user= dict(name='A', age=15, address='부천옥길자이')
#Info(**user)
Info(user)
#패킹 & 언패킹
#묶음의 형태를 묶거나 푸는 행위
# 리스트의 경우 *
# 딕셔너리의 경우 **
name, *others =user
print(name)
print(others)

#언패킹 예제
lst=[1,2,3,4,5]
number1,number2,*numbers=lst
print(numbers)
