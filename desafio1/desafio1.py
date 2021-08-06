nome = 'Jonatas Vasconcelos'
idade = 36
altura = 1.67
ano_atual = 2021
nasc = ano_atual - idade
peso = 65
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nasc}.')
