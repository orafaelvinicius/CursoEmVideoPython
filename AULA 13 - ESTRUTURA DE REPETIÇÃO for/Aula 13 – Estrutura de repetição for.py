# Laços de repetição (parte 1)

# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:
## Laço com variável de controle
# for c in range(inicio do intervalo, fim do intervalo, variável de controle):
# print(c)
# print(‘Acabou’)

# Os laços de repetição são utilizados para os casos onde você precisa repedir uma determinada operação diversas vezes (ex. abertar um botão)

# Por exemplo: Se você precisa fazer um personagem caminhar e passar por objetáculos, você pode fazer da seguinte maneira:

# laço c no intervalo(0,3)
#   se moeda:
#        pegue
#    passo
#    pula
# passo
# pega

### O nome do laço representado pela letra "c" no exemplo, pode ser alterado para qualquer nome

# Em pythom, este mesmo exemplo ficaria assim:
# for c in range(0,3)
#   if moeda:
#        pegue
#    passo
#    pula
# passo
# pega

# -- Prática
print('Repetindo conteúdo do laço')
for c in range(0,3): # - Repetindo o conteudo do laço
    print('oi')

print('Contando de 0 a 4')
for n in range(0,5): # - Contando de 0 a 4
    print(n) # - Usando a representação "n" do for para contagem

print('Contanto de 2 em 2')
for n1 in range(0, 7, 2): # - Usando a 3ª variável para pular casas da contagem
    print(n1)

print('Contando em orgem inversa sem o "0"')
for n2 in range(6, 0, -1): # - Usando a 3ª variável para eliminando o "0" ou primeiro valor
    print(n2)

print('Usando laços com variáveis')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Pular: '))
for caminho in range(i, f+1, p):
    print(caminho)
print('Contando os paços pulando {} casas'.format(p))

print('Usando laços para repetir o número digitado')
for num in range(0,3):
    n = int(input('Digite um valor: '))
print('Repetindo dados de entrada.')

print('Usando laços para fazer uma soma')
s = 0
for soma in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n # ou use apenas s += n
print('A soma de todos os valores foi {}'.format(s))
