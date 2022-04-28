#변수 : 숫자, 숫자의 합, 시작점
#조건 : 입력, 1부터 입력한 숫자까지를 더한다
num=int(input('숫자를 입력하시오'))
sum=0
start=1
while start<=num:
    sum+=start
    start+=1
print('숫자의 합 : ',sum)

#문제 2 while문을 이용하여 1cm부터 10cm까지의 출력표를 만드는 코드를 작성하시오

cm=1
print('--------------')
print('cm  ','mm   ','m')
print('--------------')
while cm<=10 :
    print(cm,cm*10,cm/100,sep='    ')
    cm+=1
print('--------------')
