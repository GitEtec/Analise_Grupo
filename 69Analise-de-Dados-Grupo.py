'''
Crie um programa que leia a idade e o sexo de varias pessoas.A cada pessoa
cadastrada, o programa devera perguntar se o usuario quer ou nao continuar.
No final mostre:
a) maiores de 18 anos
b) quantos homens foram cadastrado
c) mulheres com menos de 20 anos.
'''
maior = 0
totM20 = 0
totH = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M|F]: ')).strip().upper()[0]
        if idade >= 18:
            maior +=1
        if sexo == 'F' and idade < 20:
            totM20 +=1
        if sexo == 'M':
            totH +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S|N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Maiores de idade: {maior}')
print(f'Total de Homens: {totH}')
print(f'Mulheres com menos de 20 anos: {totM20}')



