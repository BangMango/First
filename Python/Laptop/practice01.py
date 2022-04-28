name=input('이름을 입력해주세요.\n')
age=input(name+'님의 나이를 입력해주세요\n')
age=int(age)
if age>=100 or age<=0 :
    print('제대로 된 나이를 입력해주세요.')
else:
    print('환영합니다. '+name+'님.')
    print(name+"님의 나이는 "+str(age)+"세 입니다.")
