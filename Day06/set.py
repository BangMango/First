#set
# 자료구조 중 하나로 중복 값을 가질 수 없다는 특징이 있다.
# 순서가 존재하지 않는다 ==(인덱스 활용이 불가능하다)

#set 자료구조는 {}중괄호로 또한, set() 함수를 통해 정의한다.

A={1,2,3}
B=set([2,3,4,5])
C=set("Hello, World")
print(A)
print(B)
print(C)
#.추가 add
A.add(4)
print(A)
#여러값 추가 update
A.update(B)
print(A)
#제거
A.remove(5)
print(A)
#집합의 연산처리
#SET 자료구조는 수학의 집합과 비슷하다.

print("\n--집합 D 와 집합 E--\n")
D={1,2,3,4,5}
E=set([x for x in range(1,11,2)])
print(D)
print(E)
print(D-E)#D에 대한 차집합
print(D|E)#D에 대한 합집합
print(D&E)#D에 대한 교집합
print(D^E)#D에 대한 여집합

print(D.intersection(E))
print(D.union(E))
print(D.difference(E))

#set의 성질을 이용해 중복을 제거하자.
#1. 숫자를 입력받는다 1부터 해당 숫자까지의 데이터가 리스트에 추가된다.
#2. 숫자 0을 입력 시 추가를 종료한다.
#3. 그 후 중복을 제거하여 해당 리스트를 표현한다.

lst = []
while True :
    numbers = int(input('--숫자를 입력하세요.(0 입력 시 추가 종료)'))
    if(numbers==0) :
       break;
    for number in range(1, numbers+1):
        lst.append(number)
print(lst)
lst= set(lst)
lst =list(lst)
print(lst)
