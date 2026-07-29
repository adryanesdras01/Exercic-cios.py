import random

alunos = []

while True:
    nome = input('Digite o nome do aluno ou digite (sair) para sair: ')
    if nome.lower() == 'sair':
        break
    alunos.append(nome)

if alunos:
    random.shuffle(alunos)
    print(f'A ordem de alunos fica {alunos}')
else:
    print('Nenhum aluno foi cadastrado')