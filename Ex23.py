num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'O número das unidades é {u}')
print(f'O número das dezenas é {d}')
print(f'O número das centenas é {c}')
print(f'O número dos milhares é {m}')