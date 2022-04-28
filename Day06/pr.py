#주사위 두 개 가 존재한다.
DICE = [1,2,3,4,5,6]
DICE2 = [2,3,5,7,11,13]
#두 주사위를 던졌을 때, 눈의 합으로 나올 수 있는 숫자를 전부 출력한다.
summary=[]
for number in DICE :
    for number2 in DICE2 :
        summary.append(number+number2)

result=set(summary)
print(result)
