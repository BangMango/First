money=(int)(input('금액을 입력하시오 >>'))
moneyList=[50000,10000,5000,1000,500,100,50,10]
count=0
while money!=0 :
    for index in moneyList :
         if money >= moneyList[index] :
            money=money-moneyList[index]
            count+=1

print(count)
