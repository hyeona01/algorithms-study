import sys

n = int(sys.stdin.readline())

# 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
# 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다. 
# 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.

for _ in range(n):
  lst = list(map(int, sys.stdin.readline().split()))
  caseNum = lst[0]
  students = lst[1:]
  cnt = 0

  for i in range(1, 20):
    for j in range(i):
      if students[i] < students[j]:
        # 이동 횟수
        cnt += i - j
        # 순서 조정
        tmp = students[i]
        for z in range(i, j, -1):
          students[z] = students[z-1]
        students[j] = tmp
        break

  print(caseNum, cnt)
