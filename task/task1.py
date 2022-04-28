lst=[10,1,5,2]
result=lst*2
print(result)
result.append(result[0]*2)
print(result)
result2=[]
for num in result :
    if result.index(num)%2==1 :
        result2.append(num)
print(result2)
