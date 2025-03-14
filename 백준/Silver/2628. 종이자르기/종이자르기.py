import sys

# 가로로 자르면 0, 세로로 자르면 1
x, y = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

cx = [0,x]
cy = [0,y]

for i in range(n):
  dir, leng = map(int, sys.stdin.readline().split())
  if dir == 0:
    cy.append(leng)
  elif dir == 1:
    cx.append(leng)
  
cx.sort()
cy.sort()

x_temp = 0
for i in range(len(cx)-1):
  if (cx[i+1] - cx[i]) > x_temp:
    x_temp = cx[i+1] - cx[i]
  
y_temp = 0
for i in range(len(cy)-1):
  if (cy[i+1] - cy[i]) > y_temp:
    y_temp = cy[i+1] - cy[i]
  
print(x_temp*y_temp)