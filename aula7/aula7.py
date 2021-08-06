"""
Formatação de strings
"""

nome = 'Jonatas Vasconcelos'
idade = 36
altura = 1.67
e_maior = idade > 18
peso = 65
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc, '.')
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}.')
print('{} tem {} anos de idade e seu imc é {:.2f}.'.format(nome, idade, imc))
