# 1. 모듈 : .py로 만들어진 파이썬 파일, import 키워드를 통해 module을 연결해 사용할 수 있다.
# requests(http호출 관련), matplotlib(그래프 산출), numpy(C언어 구현 벡터, 행렬등  수치 계산), pandas(데이터 가공)
# scikit-learn(과학 연산) / seaborn(머신러닝)
# 2. while문: 
import time #해당 예제에서는 다음 모듈을 사용한다.
'''
count=1
while true :
    if count==10 :
        print('BOOM!')
        break
    else :
        print(count,end=' ')
    count +=1
    #조건식의 결과를 변경할 수 있는 코드를 작성한다.
    time.sleep(1)
    #time.sleep(second) : () 안에 넣은 초 만큼 멈춘다.
print('end 이후 띄어쓰기 진행')
print('그 다음 print 작성 시 다시 enter로 초기화')

타이머 만들기
1. 시/분/초 입력
2. 해당 시간으로 부터 프로그램 진행
3. 시/분/초는 각각 24시(밤12시) / 60분 / 60초 단위로 값이 처리 됩니다.
4. 오전과 오후에 대한 처리 진행
'''

hour=int(input('시간을 입력하시오.'))
min=int(input('분을 입력하시오.'))
sec=int(input('초를 입력하시오.'))
num=int(input('몇초동안 실행할지 선택하시오.'))
count=0
prefix=''
while count<=num :
    sec+=1
    count+=1
    if sec>=60 :
        min+=1
        sec=0
    if min>=60 :
        hour+=1
        min=0
    if hour>=24 :
        hour=0

    if hour<=12 :
        prefix='오전'
    elif hour > 12 :
        prefix='오후'
    print(prefix,end=' / ')
    print(hour,min,sec, sep=':')
    time.sleep(1)
