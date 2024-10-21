palavra = 'agua'

letras_acertadas = []

while True:
  usuario = input('informe uma letra')
  if usuario in palavra:
    letras_acertadas.append(usuario)
    print(letras_acertadas)
  palavra_formada = ''
  for letra in palavra:
    if letra in letras_acertadas:
      palavra_formada += letra
    else:
      palavra_formada += '*'
  print(palavra_formada)


