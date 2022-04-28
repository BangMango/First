Users={'sKorea12':['sKorea12','kr4812']}
while True:
    value=int(input('1.새 아이디 생성 \n2.기존 아이디 로그인 \n3.프로그램 종료 >>'))
    if value==1 :
        newID=input('회원가입할 아이디를 입력하시오.')
        if newID in Users.keys() :
            print('이미 존재하는 아이디입니다.')
        else :
            newPW=input('비밀번호를 입력하시오.')
            newPW_Check=input('비밀번호를 다시 입력하시오.')
            if newPW == newPW_Check :
                Users[newID]=[newID,newPW]
    elif value==2 :
        ID=input('로그인할 아이디를 입력하시오.')
        if ID not in Users.keys() :
            print('존재하지 않는 아이디입니다.')
        elif ID in Users.keys() :
            PW=input('비밀번호를 입력하시오.')
            if PW in Users.get(ID) :
                print(ID,'님! 로그인에 성공하셨습니다!')
                break;
            else :
                print('잘못된 비밀번호입니다.')
    elif value==3 :
        print('프로그램이 종료됩니다.')
        break
    else :
        print('잘못된 입력값입니다.')
