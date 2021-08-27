# Aula 7 – Operadores Aritméticos

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Quantos metros tem sua parede? '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('{} metros é igual a {:.0f}km, {:.0f}hm, {:.0f}dam, {:.0f}dm, {:.0f}cam e {:.0f}mm.'.format(m, km, hm,dam, dm, cm, mm))
