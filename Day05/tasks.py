nums=(input('데이터를 몇번 추가하시겠습니까?'))
stack=[]
if nums :
    num=int(nums)
    for e in range(num) :
        stack.append((int(input('숫자를 입력해주세요.'))))
print('-- 리스트 생성 완료 --')
print('현재 리스트 : ',stack,sep='')
while True :
    cos=input('push, pop, peek, empty, close >>')
    if cos=='push' :
        stack.append(int(input('추가할 숫자를 입력하시오.')))
    elif cos=='pop' :
        if stack :
            del stack[-1]
        elif not stack :
            print('스택 내부에 데이터 값이 없습니다.')
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

print('--스택 구성 완료--')
print('현재 리스트:',stack,sep='')
lst=[]
lst.extend(stack)
lst.reverse()
print('스택 순서 :',lst,sep='')
