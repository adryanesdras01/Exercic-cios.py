d = int(input('Qual a quantidade de dias alugados?: '))
k = float(input('Quantos km foram rodados?: '))
p = d * 60 + k * 0.15
print(f'O valor a ser pago pelo aluguel do carro é de R${p:.2f}')