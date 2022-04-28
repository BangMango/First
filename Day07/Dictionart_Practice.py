items={'제주 삼다수' :[950,10],
      '삼각김밥' : [1100,5],
      '벗겨먹는 고오스' : [1500,1]}
enter=input('아이템의 이름을 입력하시오')
if enter not in items.keys() :
    print('해당 품목은 존재하지 않습니다.')
else :
    print(items[enter][1])
while True :
    enter2=input('아이템의 이름을 입력하시오')
    if enter2 == '끝' :
        print('프로그램을 종료합니다.')
        break;
    elif enter2 not in items.keys() :
        value=input('추가할 아이템의 가격을 입력하시오.')
        count=input('추가할 아이템의 수량을 입력하시오.')
        items[enter2]=[value,count]
    elif enter2 in items.keys() :
        value=input('수정할 아이템의 가격을 입력하시오.')
        count=input('추가할 아이템의 수량을 입력하시오.')
        items[enter2]=[value,count]
