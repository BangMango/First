address=''
ID=input('아이디로 사용할 문장을 입력해주세요. 최대 글자는 6글자까지 가능합니다.\n')
if len(ID) > 6 :
    print('아이디가 6글자를 초과했습니다.')
else: 
    select=int(input('다음 주소 중 하나를 선택해주세요. \n1.네이버 2.지메일 3.페이스북 4.다음 \n'))
    if select==1 :
        address='naver.com'
    elif select==2 :
        address='gmail.com'
    elif select==3 :
        address='facebook.com'
    elif select==4 :
        address='hanmail.com'
    
    print('ID가 생성되었습니다.')
    print(ID,address,sep='@')


#elif문 : if문 다음에 작성할 수 있는 문법으로 if문의 결과가 참이 아닐 때,
#elif의 조건의 결과라 참이라면, 해당 명령문을 실행한다 ex)JAVA else if문
    
