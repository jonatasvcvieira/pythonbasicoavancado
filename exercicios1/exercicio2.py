# Desejando bom dia, boa tarde e boa noite ao usuario de acordo com horario digitado.

horario = input('Digite um horário entre 0 e 23:')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horário deve estar entre ) e 23.')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite')
else:
    print('Por favor, didgite um horário entre 0 e 23.')


