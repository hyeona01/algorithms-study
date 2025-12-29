flags = [0] * 10000 # 0부터 9999까지

for i in range(1, 10000):
    constructor = i + (i // 1000) + (i // 100 % 10) + (i // 10 % 10) + (i % 10) # 각 자리수 더하기
    if constructor < 10000:
        flags[constructor] = 1 # 생성자가 있으면 표시

for i in range(1, 10000):
    if flags[i] == 0:
        print(i)


