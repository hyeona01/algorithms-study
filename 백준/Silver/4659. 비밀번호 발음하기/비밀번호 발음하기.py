import sys

# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

password = sys.stdin.readline().strip()
vowels = ['a', 'e', 'i', 'o', 'u']

def step1(pw):
  for v in vowels:
    if v in pw:
      return True
  return False

def step2(pw):
  cnt = 1
  prev_type = None

  for i in range(len(pw)):
    if pw[i] in vowels:
      curr_type = 'vowel'
    else:
      curr_type = 'consonant'
    
    if curr_type == prev_type:
      cnt += 1
    else:
      cnt = 1
      prev_type = curr_type

    if cnt == 3:
      return False

  return True

def step3(pw):
  for i in range(len(pw)-1):
    if pw[i] == pw[i+1] and pw[i] not in ['e', 'o']:
      return False
  return True

# 메인 실행 코드
while password != "end":
  if step1(password) and step2(password) and step3(password):
      print(f"<{password}> is acceptable.")
  else:
      print(f"<{password}> is not acceptable.")

  password = sys.stdin.readline().strip()