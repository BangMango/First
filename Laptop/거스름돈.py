money=(int)(input())
moneyList=[50000,10000,5000,1000,500,100,50,10]
count=0
while money!=0 :
    for index in moneyList :
         while money >=index :
            money-=index
            count+=1
print(count)
