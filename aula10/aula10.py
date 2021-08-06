'''
Operadores Relacionais
==  igualdade
>   maior que
>=  maior ou igual
<   menor que
<=  menor ou igual
!=  diferente

num1 = 2        #int
num2 = '2'      #str
variavel = 'valor'
expressao = num1 == num2
expressao1 = num1 > num2
print(2 == 2)       #perguntando se são iguais
print(2 == 1)
print(2 == '2')
print(num1 == num2)
print(expressao)
print(expressao1)


nome = str(input('Qual é o seu nome? '))
idade = int(input('Qual é a sua idade? '))
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'NÂO pode pegar o empréstimo.')
'''

nome = str(input('Qual é o seu nome? '))
idade = int(input('Qual é a sua idade? '))
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'NÂO pode pegar o empréstimo.')
