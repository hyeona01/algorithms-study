import sys

N = int(sys.stdin.readline())

# words = [sys.stdin.readline().rstrip() for i in range(N)]
words = []
for i in range(N):
  word = sys.stdin.readline().rstrip()
  words.append({'len': len(word), 'word': word})

# 1. 길이가 같으면 사전 순으로
step1 = sorted(words, key=(lambda x: x['word']))

# 2. 길이가 짧은 것부터 
step2 = sorted(step1, key=(lambda x: x['len']))

# 3. 중복된 단어는 제거
printed = set() # 출력된 단어 확인용

for item in step2:
    if item['word'] not in printed:
        print(item['word'])
        printed.add(item['word'])