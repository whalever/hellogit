#오버테일 파이썬 스터디 1주차
##1
###입력
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

###평균
avg = int((n1+n2+n3+n4+n5)/5)

###중앙
numbers = [n1, n2, n3, n4, n5]
#########맞다 크기순 정렬이 안돼있었구나... sort 함수는 안배웠어요~~~~
numbers.sort()
center = numbers[2]

###출력
print('평균값: ', avg)
print('중앙값: ', center)

###답답해
print('')





##2
###입력
A=int(input())
B=int(input())

###계산, 출력
print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
print(A%B)

###답답해
print('')





##3
###입력
A=int(input())
B=int(input())
C=int(input())

###계산, 출력
print((A+B)%C)
print((A%C + B%C)%C)
print((A*B)%C)
print((A%C*B%C)%C)

###답답해
print('')





##4
###예...? 고양이요..?
print('\    /\ ')
print(' )  ( \')')
print('(  /  )')
print(' \(__)|')

###한줄로 해보자
print('\n')
print('\    /\ \n )  ( \')\n(  /  )\n \(__)|')

####for이랑 while을 써서 고양이 만들 수 있다고요....? 대체 어떻게..?
