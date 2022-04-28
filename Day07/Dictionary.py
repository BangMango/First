player=dict(hp=50,mp=50,lv=1,atk=70,Def=12)

#반복문을 활용해 dict걊 확인
for key in player:
    print(key, end=' ')
    
#딕셔너리명.keys()
print('\n',player.keys())

#dict value값 확인
print('\n', player.values())
for value in player.values() :
    print(value, end=' ')
#dict명.get(key) 키에 해당하는 값을 가져온다.
print('\n', player.get('hp'))

#존재하는 딕셔너리에 값을 추가 / 수정
player['hp']=500

print(player)
#새로운 값 추가
player['money']=10000
#딕셔너리 값 제거
del player['money']
