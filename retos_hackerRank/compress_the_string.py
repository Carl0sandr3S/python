import itertools
STDIN =input()
l = [int(i) for i in STDIN]
lista = [(k, list(g)) for k, g in itertools.groupby(l)]
lista_aux = []
for i in lista:
  lista_aux.append((len(i[1]), i[0]))
print(" ".join(str(x) for x in lista_aux))
