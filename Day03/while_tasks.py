import time
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

