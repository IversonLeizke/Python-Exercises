n = int(input('Insira um número de 0 a 9999: '))
print(f'unidade: {n // 1 % 10}')
print(f'dezena : {n // 10 % 10}')
print(f'centena: {n // 100 % 10}')
print(f'milhar : {n // 1000}')
