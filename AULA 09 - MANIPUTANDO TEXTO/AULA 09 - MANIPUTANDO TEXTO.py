# Aula 9 – Manipulando Texto
## Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

# FORMAS DE FATIAMENTO
## frase = Curso em vídeo
## frase[9] - pega apenas uma letra da variável
## frase[9:13] - pega o intervalo entre o caractere 9 ao 13 (O último número será excluído).
## frase[9:21:2] - pega o intervalo escolhido e o segundo ":" cria um intervalo de saltos vai pulando de acordo com o intervalo
## frase[:5] - pega tudo que estiver antes dos ":". (O último caractere é excluido sempre)
## frase[15:] - pega os caracteres estiverem a partir dos ":" e ignora o começo. (do número pra frente)
## frase[9::3] - pega os caracteres a partir do primeiro número e pula casas de acordo com o último número.

# ANALISE
## frase = Curso em vídeo
# len é o mesmo que comprimento
## len(frase) - mostra o comprimento da variável
## frase.count('o') - faz a contagem do 'o' ou qualquer caractere dentro do ''.
## frase.count('o',0,13) - faz a contagem com número de caracateres fatiado
## frase.find('deo') - find é o mesmo que "encontrar", então mostra onde começa o texto que estiver dentro das ''.
## frase.find('???') - quando você coloca uma str que não existe na frase, ele retorna -1 (caractere inexistente)

## 'Curso' in frase - o operador "in" é o mesmo que perguntar "no/na" frase

# TRANSFORMAÇÃO
## frase = Curso em vídeo
## frase.replace('Phyton','Android') - O 'replace' faz a frase ser sbustituida de forma secundária
## frase.uppper() - Deixa a string toda em letra maiúscula
## frase.lower() - Deixa a string toda em letras minúsculas
## frase.capitalize() - Deixa todos os caracteres em minúsculo e só a primeira letra em maiúsculo
## frase.title() - Analisa de forma mais profunda e faz o captalize no começo de todas as palavras

## frase.stip() - Remove os espaços excedeentes no início e no fim da string
## frase.rstip() - faz o strip começar da direita e remover só os espaços do fim
## frase.lstip() - faz o strip começar da direita e remover só os espaços do começo

### utilizando o "r" ou "l" no começo da função, faz a função começar da direita ou esquerda.


# DIVISÃO
## frase.split() - Faz uma lista com todas as palavras da cadeira de caracteres separadamente.

# JUNÇÃO
## '-'.join(frase) - O join faz a junção de uma lista e coloca o caractere dentro do '' na separação de todas as palavras da lista

