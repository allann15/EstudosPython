valor = '73167176531330624919225119674426574742355349194934'
acumulador = 0

for numeros in range(0,len(valor) - 4):
 produto = int(valor[numeros]) * int(valor[numeros+1]) * int(valor[numeros+2]) * int(valor[numeros+3]) * int(valor[numeros+4])
 if produto > acumulador:
  acumulador = produto
  guardar_numeros = [valor[numeros],valor[numeros+1],valor[numeros+2],valor[numeros+3],valor[numeros+4]]
  index = numeros

print(acumulador)
