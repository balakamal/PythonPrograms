n = int(input())
wordset = []
for _ in range(n):
    wordset.append(input())

m = int(input())
sentences = []
for _ in range(m):
    sentences.append(input())

count = {}

for i in range(len(wordset)):
    count[wordset[i]] = -1
    for j in range(len(wordset)):
        if(sorted(wordset[i])) == sorted(wordset[j]):
            count[wordset[i]] += 1
# print(count)


for i in sentences:
    res = 0
    for j in i.split():
        if(j in wordset):
            res += count[j] * 2
    print(res)
