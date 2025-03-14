def f(n, a, b, c):
  if(n == 1):
    print(a, c, sep = " ")
  else:
    f(n-1, a, c, b) #1단계
    f(1, a, b, c) #2단계
    f(n-1, b, a, c) #3단계

n = int(input()) #입력
print(2**n-1) #이동횟수 출력
if(n <= 20): #함수 조건
  f(n, 1, 2, 3) #함수 호출