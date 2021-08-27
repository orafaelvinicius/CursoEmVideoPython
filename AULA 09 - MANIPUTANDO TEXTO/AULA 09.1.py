frase = 'Curso em vídeo Phyton'
print(frase[:5])
### DICA DE PRINT: USE 3 ASPAS PARA IMPRIMIR UM TEXTO GRANDE

frase = 'Curso em vídeo Phyton'
print(frase.count('o'))              # CONTANDO LETRAS.

frase = 'Curso em vídeo Phyton'
print(frase.upper().count('o'))      # Lembre que existe variação de maiusculo e minusculo

frase = '  Curso em vídeo Phyton'
print(len(frase))                    # USE FUNÇÕES INTERNAS. Len para ver o tamanho do texto

frase = '   Curso em vídeo Phyton'
print(len((frase.strip())))          # USE FORMATAÇÃO DENTRO DE FUNÇÕES. FUNCIONA!

frase = 'Curso em vídeo Phyton'
print(((frase.replace('Phyton', 'Android')))) # ALTERA O NOME DO VALOR, MAS NÃO FAZ ALTERAR A STRING, POIS ELA É IMUTÁVEL!

frase = 'Curso em vídeo Phyton'
print(frase.find('video'))              # USE find PARA ENCONTRAR ALGUMA FRASE

frase = 'Curso em vídeo Phyton'
print(frase.lower().find('video'))      # PARA PROCURAR FRASES EM MINUSCULOS

frase = 'Curso em vídeo Phyton'
print(frase.split())                    # USE split PARA CRIAR LISTAS COM A FRASE

frase = 'Curso em vídeo Phyton'
dividido = frase.split()
print(dividido[2][3])                      # EXEPLO DE USO DO SPLIT PARA SEPARAR ITENS DA LISTA
