import sys

A, B, C = map(int, sys.stdin.readline().split())

# 짝수인 경우 : A^B = (A^(B/2)) * (A^(B/2))
# 홀수인 경우 : A^B = (A^(B//2)) * (A^(B//2)) * A

# 모듈러 연산 : 곱셈이 커지기 전에 중간중간에 나머지를 취해도 최종 결과가 동일하다
# (A * B) % C = ((A % C) * (B % C)) % C

def recur_multi(A, B):
    if B == 0:
        return 1
    half = recur_multi(A, B // 2) % C
    if B % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * A) % C

print(recur_multi(A, B))
