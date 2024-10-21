acumulador1 = 0
acumulador2 = 0
for valor in range(1,101):
  acumulador1 += valor**2
  acumulador2 += valor
print(acumulador2**2 - acumulador1)
