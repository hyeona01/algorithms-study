T = int(input())

for _ in range(T):
  test = input()
  valid = 0

  for i in range(len(test)):
    check = test[i]

    if check == "(" : 
      valid += 1 

    elif check == ")" :
      valid -= 1

    if valid < 0 : 
      break

  if valid == 0 :
    print("YES")
  else : print("NO")
