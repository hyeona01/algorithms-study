import sys

input = [int(sys.stdin.readline()) for _ in range(9)]

print(max(input))
print(input.index(max(input))+1)