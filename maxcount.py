from typing import Counter
s = list(input())
cnt = Counter(s)
print(max(cnt.values()))
