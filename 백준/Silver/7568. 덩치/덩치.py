import sys

n = int(sys.stdin.readline())
people = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    rank = 1
    for j in range(n):
        if i != j:
            if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                rank += 1
    print(rank, end=" ")