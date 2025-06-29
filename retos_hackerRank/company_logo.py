from collections import Counter

#link https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

s = input()
conteo_ = 0
conteo = Counter(s)
palabras_ordenadas = {}
dict_aux  = dict(sorted(conteo.items(),reverse=True, key=lambda item: item[1]))
for key, value in dict_aux.items():
  palabras_ordenadas[value] = [key] if value not in palabras_ordenadas.keys() else palabras_ordenadas[value] + [key]

for key, value  in list(palabras_ordenadas.items())[0:3]:
  value_aux = sorted(value)[0:3]
  for i in value_aux:
    print(key, i)
    conteo_ += 1
    if conteo_==3:
      break

  if conteo_==3:
    break