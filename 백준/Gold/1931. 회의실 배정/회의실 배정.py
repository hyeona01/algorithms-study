import sys

N = int(sys.stdin.readline())
time_table = []

for _ in range(N):
  st, en = map(int, sys.stdin.readline().split())
  time_table.append((st, en))
time_table.sort(key= lambda x: x[0])
time_table.sort(key= lambda x: x[1])

remain = [time_table[0][1]]
for i in range(1, N):
  s, e = time_table[i]

  if remain[-1] <= s: # 이미 시작한 회의의 끝나는 시간이 새로 시작하는 회의의 시작 시간보다 이르거나 같을 때
    remain.append(e)

print(len(remain))