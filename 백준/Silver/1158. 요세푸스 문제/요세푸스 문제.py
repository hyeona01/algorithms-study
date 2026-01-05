N, K = map(int, input().split())
arr = []

for i in range(1, N+1):
    arr.append(i)

current = 0
print("<", end='')

deleted_idx = (current + K - 1) % len(arr)

print(arr.pop(deleted_idx), end='')
current = deleted_idx - 1

while len(arr) > 0:
    deleted_idx = (current + K) % len(arr)

    # 순열에서 삭제
    print(', ', end='')
    print(arr.pop(deleted_idx), end='')
    # 다음 순서
    current = deleted_idx - 1

print(">")