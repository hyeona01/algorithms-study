N = int(input())
arr = []
cnt = {}

for _ in range(N):
    num = int(input())
    arr.append(num)
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1

arr.sort()

print(round((sum(arr) / N))) # 산술평균
print(arr[N//2]) # 중앙값

max = 0
candidates = []
for key, value in cnt.items():
    if value > max:
        max = value
        candidates = [key]
    elif value == max:
        candidates.append(key)
candidates.sort()
print(candidates[1] if len(candidates) > 1 else candidates[0]) # 최빈값

print(arr[-1] - arr[0]) # 범위

