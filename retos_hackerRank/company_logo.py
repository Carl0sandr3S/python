from collections import Counter

#link https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

s = input()
count = Counter(s)
sort = sorted(count.items(), key = lambda x: (-x[1], x[0]))
print("\n".join(f"{a} {b}" for a,b in sort[:3]))