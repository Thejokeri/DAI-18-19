
def criba_eratostenes(n):
  multiplos = set()
  for i in range(2, n+1):
    if i not in multiplos:
      print(i, end=" ")
      multiplos.update(range(i*i, n+1, i))

criba_eratostenes(1000)

