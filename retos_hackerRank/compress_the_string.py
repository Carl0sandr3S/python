import itertools

STDIN =input()
entrada = list(map(int, STDIN))
for key,group in  itertools.groupby(entrada):
  print(f"({len(list(group))}, {key})", end=" ")