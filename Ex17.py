import math
o = float(input('Qual o valor do seu cateto oposto?: '))
a = float(input('Qual o valor do seu cateto adjacente: '))
h = math.pow(o) + math.pow(a)
print(f'O valor da sua hipotenuas é {h}')