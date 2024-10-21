
cidade1 = input('informe o nome da primeira cidade: ')

cidade2 = input('informe o nome da segunda cidade: ')

dicionario_cidades = {
  'Alabaster' : {'Birmingham' : 24, 'Montgomery' : 71},
  'Birmingham' : {'Huntsville' : 103, 'Tuscaloosa' : 59},
  'Demopolis' : {'Mobile' : 141, 'Montgomery' : 101, 'Tuscaloosa' : 65},
  'Mobile' : {'Montgomery' : 169},
  'Montgomery' : {'Tuscaloosa' : 134}
}
distancia = 0
for cidade in dicionario_cidades:
  if cidade1 in cidade or cidade2 in cidade:
    for nome_cidade1, valor1 in dicionario_cidades[cidade1].items():
      if nome_cidade1 == cidade1 or nome_cidade1 == cidade2:
        distancia = valor1
        break
      for nome_cidade2, valor2 in dicionario_cidades[cidade2].items():

        if nome_cidade1 == nome_cidade2 :
          distancia = valor1 + valor2
print(distancia)
