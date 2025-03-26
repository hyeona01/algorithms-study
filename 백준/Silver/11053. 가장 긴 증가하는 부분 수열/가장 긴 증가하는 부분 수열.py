import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def find_idx(lst, x):
  start = 0
  end = len(lst) - 1
  while start <= end:
    mid = (start + end) // 2

    if x == lst[mid]:
      return mid
    elif x < lst[mid]:
      end = mid - 1
    elif x > lst[mid]:
      start = mid + 1
  return start

lis = []
if n == 1:
  lis.append(arr[0])
if n == 2:
  if arr[1] > arr[0]:
    lis.append(arr[0])
    lis.append(arr[1])
  else:
    lis.append(arr[0])

elif n > 2:
  for i in range(n):
    if not lis:
      lis.append(arr[i])
    elif lis[-1] < arr[i]:
      lis.append(arr[i])
    else:
      lis[find_idx(lis, arr[i])] = arr[i]

# print(lis)
print(len(lis))