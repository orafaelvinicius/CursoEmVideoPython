# Aula 12 – Condições Aninhadas
## Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

# uso do ELIF para montar a estrura "SE NÃO SE", assim você pode fazer varios "SES" dentro do projeto
## ex:
#   if carro.esquerda():
#       bloco 1
#   elif carro.direita():
#       bloco 2
#   elif carro.ré():
#       bloco 3
#   else:
#       bloco 4
## O uso de "else" e "elif" são opcionais caso a estutura seja simplificada.

#-- Prática
##-- Estrutura condicional aninhada.
nome = str(input('Qual é o seu nome: '))
if nome == 'Rafael':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Letícia Karol':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}'.format(nome))




