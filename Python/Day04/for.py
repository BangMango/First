#range(숫자) : 0부터 숫자 -1까지릐 범위를 가지는 숫자형 리스트로 만드는 함수

#list : 여러가지 데이터를 묶어서 표현하는 자료구조
#추가, 삭제, 수정등의 작업을 할 수 있는 대표 자료구조

#자료구조(data structure): 데이터를 효율적으로 사용하기 위해 묶어 표현하고,
#데이터 활용을 위한 다양한 기능을 포함한 개념

for number in range(10): #range(시작부분, 끝부분) : 시작부분부터 끝부분-1까지 범위
    print (number)

    jjak=0

for number in range(2,101,2) :
    jjak+=number

print(jjak)

#연습문제 
#【문제 1】 다음 아래에는 split 함수에 대한 설명이 작성되어 있습니다.
#해당 기능을 활용하여 multiline에 적힌 문장을 다음 실행 결과처럼 나눠서 출력하시오.
#문자열.split() : split 함수는 문자열을 공백을 기준으로 문자열을 나누어줍니다.

multiline = '안녕하세요. 오늘은 파이썬 수업이 있는 날입니다. 시간은 총 3시간입니다.'
for value in  multiline.split():
    print(value)
print('단어 갯수 :',len(multiline.split()))
