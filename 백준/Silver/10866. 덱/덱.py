arr = []

def push_front(arr, x):
    arr.insert(0, x)
    return arr

def push_back (arr, x):
    arr.append(x)
    return arr

def pop_front(arr):
    if len(arr) > 0:
        print(arr.pop(0))
        return arr
    else:
        print(-1)
        return arr

def pop_back (arr):
    if len(arr) > 0:
        print(arr.pop(len(arr)-1))
        return arr
    else:
        print(-1)
        return arr

def size (arr):
    print(len(arr))
    return arr

def empty (arr):
    if len(arr) > 0:
        print(0)
        return arr
    else:
        print(1)
        return arr

def front (arr):
    if len(arr) > 0:
        print(arr[0])
        return arr
    else:
        print(-1)
        return arr

def back (arr):
    if len(arr) > 0:
        print(arr[-1])
        return arr
    else:
        print(-1)
        return arr

N = int(input())
result = []
for _ in range(N):
    cmd = input().split(' ')

    if cmd[0] == 'push_back':
        push_back(result, int(cmd[1]))
    
    elif cmd[0] == 'push_front':
        push_front(result, int(cmd[1]))
    
    elif cmd[0] == 'pop_front':
        pop_front(result)
    
    elif cmd[0] == 'pop_back':
        pop_back(result)
    
    elif cmd[0] == 'size':
        size(result)
    
    elif cmd[0] == 'empty':
        empty(result)
    
    elif cmd[0] == 'front':
        front(result)
    
    elif cmd[0] == 'back':
        back(result)
    else:
        print("잘못 입력하셨습니다.")