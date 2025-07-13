from collections import Counter
n, m = input().split()
array_n = input().split()
a = input().split()
b = input().split()
conteo_array_n = Counter(array_n)

def no_idea (conjunto,  array_n):
  valores_comunes= set(array_n.keys()) & set (conjunto)
  cruce_diccionarios = filter(lambda item: item[0] in valores_comunes, array_n.items())
  return sum(dict(cruce_diccionarios).values())

print(no_idea(a,conteo_array_n) - no_idea(b,conteo_array_n) )