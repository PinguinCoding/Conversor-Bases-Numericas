def conversao_decimal(decimal, base):
    tipo = ''
    while decimal > 0:
        tipo += str(decimal%base)
        decimal//=base
    return tipo[::-1]

num = int(input('Insira um número para ser convertido: '))
print('Converter para binário (1) \n'
    'Converter para octal (2) \n'
    'Converter para hexadecimal (3)')
con = int(input('Insira para qual base deseja converter: '))

if con == 1:
    print(f'A conversão do número decimal {num} para binário é ' + conversao_decimal(num, 2))
elif con == 2:
    print(f'A conversão do número decimal {num} para octal é ' + conversao_decimal(num, 8))
elif con == 3:
    print(f'A conversão do número decimal {num} para hexadecimal é ' + conversao_decimal(num, 16))
else:
    print('Opção inválida!')
