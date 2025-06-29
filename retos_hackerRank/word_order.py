from collections import Counter
#link https://www.hackerrank.com/challenges/word-order/problem
STDIN = int(input())
palabras = [input() for _ in range(STDIN)]
print(len(set(palabras)))
contador = dict(Counter(palabras))
print(" ".join(str(x) for x in list(contador.values())))