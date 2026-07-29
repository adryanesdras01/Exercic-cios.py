import random

a = input('Digite o nome do Primeiro aluno: ')
b = input('Digite o nome do Segundo aluno: ')
c = input('Digite o nome do Terceiro aluno: ')
d = input('Digite o nome do Quarto aluno: ')
lista = [a, b, c, d]
random.shuffle(lista)
print(f'A ordem de apresentação será: ')
print(f'{lista}')
