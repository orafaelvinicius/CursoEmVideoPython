# Aula 11 – Cores no Terminal

## Utilizando o padrão ANSI (Escape sequence). Padrão de normalização internacional. Sempre começa com \+codigo

# ANSI para cores
## A faixa de cores que funciona melhor para python é a 033, ou \033[m
## Entre o [...m vocÊ pode preencher até 3 código separados por ;
### O primeiro código do [;;m é do comportamento ( STYLE da fonte;
### O segundo código do [;;m é o cód da cor do TEXT;
### O terceiro código do [;;m é o cód da cor do BACKGROUND;
### ex: \033[0;33;44m]

## códigos para STYLE
# 0 = none (padrão = sem nada)
# 1 = bold (negrito)
# 4 = underline (sublinhado)
# 7 = negative (cores invertidas)

## códigos para TEXT
# 30 = branco
# 31 = vermelho
# 32 = verde
# 33 = amarelo
# 34 = azul
# 35 = magenta
# 36 = ciano
# 37 = cinza
# Para colocar mais cores, é necessário importar uma biblioteca

## códigos para BACKGROUND
# 40 = branco
# 41 = vermelho
# 42 = verde
# 43 = amarelo
# 44 = azul
# 45 = magenta
# 46 = ciano
# 47 = cinza

# --- Exemplos práticos
#   \033[0;30;41m #- Letra padrão; texto branco; fundo vermelho
#   \033[4;33;44m #- Letra subplinhada; texto amarelo; fundo azul
#   \033[1;35;43m #- Letra negrito; texto magenta; fundo amarelo
#   \033[30;42m   #- Letra ?padrão?; letra branca; fundo verde
#   \033[m         #- Desfaz as configurações e deixa o padrão do terminal
#   \033[7;30m     #- Deixa o fundo sempre branco

# --- Prática
print('\033[1;34;40mOlá mundo!\033[m')

# - Inserindo cores dentro do texto
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e o \033[31m{}\033[m'.format(a, b))

# - Inserindo cores na formatação
nome = 'Rafael'
print('Olá, muito prazer em te conhecer {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))  ## Lembrar sempre de colocar o cód entre '' no format

# - Inserindo a cores a partir de uma variável
nome = 'Rafael'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'preto-e-branco': '\033[7;30m'}

print('Olá, muito prazer em te conhecer {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))


# --- DESAFIOS
