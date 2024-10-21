digitos = input('Informe quantos valores serão utilizados na operação: ')

try:
  digitos_inteiro = int(digitos)

except:
  print('Este não é um número inteiro')

contador = 0
lista_numeros = [0]
resultado = 0
for contador in range(digitos_inteiro):
  if contador == digitos_inteiro:
    break
  if contador >= 1:
    operacao = input('Escolha a operação, 1 - adição; 2 - subtração; 3 - multiplicação; 4 - Divisão, 5 - igual: ')
    valor = float(input('Informe o valor: '))
    if operacao == '1' or operacao == 'adicao':
      resultado = lista_numeros[-1] + valor
      lista_numeros.append(resultado)
    elif operacao == '2' or operacao == 'subtracao':
      resultado = lista_numeros[-1] - valor
      lista_numeros.append(resultado)
    elif operacao == '3' or operacao == 'multiplicacao':
      resultado = lista_numeros[-1] * valor
      lista_numeros.append(resultado)
    elif operacao == '4' or operacao == 'divisão':
      resultado = lista_numeros[-1] / valor
      lista_numeros.append(resultado)
    elif operacao == '5' or operacao == 'igual':
      break
  if contador == 0:
    valor = float(input('Informe o valor: '))
    lista_numeros.append(valor)
  contador += 1
print(resultado)
