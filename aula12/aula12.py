'''
usuario = input('Digite seu usuário:')
qtd_carcteres = len(usuario)

if qtd_carcteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')
 '''

'''
str1 = input('Digite alguma coisa:')
str2 = input('Digite outra coisa:')

print(f'A quantidade total de caracteres digitados foi {len(str1) + len(str2)}')

'''

print(len(str1))
print(str1.__len__())

# len não funciona com int, float e bool

