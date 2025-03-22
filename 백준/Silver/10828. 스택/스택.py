import sys

N = int(sys.stdin.readline())
list = []

for i in range(N):
  mode = sys.stdin.readline().strip()
  if mode.find(" ") != -1 : 
    mode, num = map(str, mode.split())

  if mode == "push":
    list.append(int(num))
  elif mode == "pop":
    if len(list)>0 : print(list.pop())
    else : print(-1)
  elif mode == "size":
    print(len(list))
  elif mode == "empty":
    if len(list)>0 : print(0)
    else : print(1)
  elif mode == "top":
    if len(list)>0 : print(list[-1])
    else : print(-1)
  
# 알 수 없는 시간초과로 서칭해본 결과, input으로 입력받은 것이 이유였다!
# 앞으로는 sys 방법으로 입력받아야겠다.