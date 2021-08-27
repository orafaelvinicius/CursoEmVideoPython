# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA COM O NOME "SANTO". (???KKKK)

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')

### O programa quebra quando o nome da cidade não está no inicio do input