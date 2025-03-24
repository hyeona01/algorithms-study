import sys
from collections import deque

string = sys.stdin.readline().strip()

# string = deque('(()[[]])([])')
temp = []

def solution(string):
  for ch in string:
    if ch == '(' or ch == '[': # 열린 괄호라면
      temp.append(ch)

    elif ch == ')':
      val = 0
      while temp:
        top = temp.pop()
        if top == '(':
          temp.append(2 if val == 0 else val * 2)
          break
        elif isinstance(top, int):
          val += top
        else:
          # 괄호 불일치
          return 0
      else:
        # 열림 괄호 못 찾고 끝났다면
          return 0

    elif ch == ']': # 닫힌 괄호라면
      val = 0
      while temp:
        top = temp.pop()
        if top == '[':
          temp.append(3 if val == 0 else val * 3)
          break
        elif isinstance(top, int):
          val += top
        else: 
          return 0
      else: 
        return 0
  
  # 마지막에 temp에 괄호가 남아있으면 잘못된 경우
  for item in temp:
    if not isinstance(item, int):
      return 0

  return sum(temp)

print(solution(string))