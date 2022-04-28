#리스트의 문법
lst=[]
lst2=[2,3,4,5]
#리스트명.append(값) 해당 값을 리스트에 넣어준다.
lst.append(1)
#리스트명.extends(다른 리스트) : 열거형으로 만들어진 값의 각각의 요소를 리스트에 추가
#lst.extend(lst2)
#리스트명.remove(값)
lst.remove(1)
 
lst.append(lst2)
lst.extend(lst2)


#묶음 내부에 있는 값을 제거하기 위해서는 remove가 아닌
#del 리스트명[묶음 인덱스][묶음 내부 삭제를 원하는 인덱스]
print(lst)
#del 리스트명[인덱스값] : 해당 리스트의 인덱스 번호에 있는 값을 제거한다.
del lst[0][1]
print(lst)

num=len(lst)
'''
for e in range(num) :
    del lst[0]
'''

for e in lst[:] :
    lst.remove(e)
print(lst)

print(lst2)
print(lst2.pop())
print(lst2)
'''
push 스택에 요소 추가
pop 스택 마지막 요소 삭제
peek 스택 마지막 값 출력
empty 스택이 비어있는지 확인
'''
#원하는 횟수만큼 숫자를 추가해 리스트를 구성한다.
num=int(input('데이터를 몇번 추가하시겠습니까?'))
stack=[]
for e in range(num) :
    stack.append(input('숫자를 입력해주세요.'))

print('-- 리스트 생성 완료 --')
print('현재 리스트 : ',stack,sep='')
cos=input('push, pop, peek, empty, close >>')
while cos != 'close' :
    if cos=='push' :
        stack.append(int(input('추가할 숫자를 입력하시오.')))
    elif cos=='pop' :
        del stack[-1]
    elif cos=='peek' :
        print(stack[-1])
    elif cos=='empty' :
        if stack :
            print('비어있지 않습니다.')
        elif not stack :
            print('비어있습니다.')
    elif cos=='close' :
        break;
    else :
        print('잘못된 입력값입니다.')

    cos=input('push, pop, peek, empty, close >>')

print('--스택 구성 완료--')
print('현재 리스트:',stack,sep='')
stack.reverse()
print('스택 순서 :',stack,sep='')
