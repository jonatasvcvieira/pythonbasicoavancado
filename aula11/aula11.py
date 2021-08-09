'''
Operadores Lógicos
and, or, not
in e not in

#and
#Verdadeiro e falso = falso
#Verdadeiro e verdadeiro = verdadeiro
#Falso e verdadeiro = falso

comparação1 and comparação2

# or
#Verdadeiro ou falso = verdadeiro
#Se qualquer uma retornar verdaeiro o resultado será verdadeiro

comparação3 ou comparação4

#not
# Not mostrará o inverso da operação
a = ''
b = 0

if not b:
    print('Por favor, preencha o valor de B.')

#in e not in
#Procura se existe a informação dentro da variavel

#in

nome = Jonatas

if 'Jo' in name:
    print('Existe')
else:
    print('Não existe')

#not in

nome = Vasconcelos

if 'Jo' not in name:
    print('Executei'.)
else:
    print('Existe o texto.')

usuario = input('Nome de usuário:')

'''

usuario = input('Nome de usuário:')
senha = input('Senha do usuário:')

usuario_bd = 'jonatas'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário e senha inválidos.')

