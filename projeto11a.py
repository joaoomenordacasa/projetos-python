n1 = str(input('Digite seu nome completo :')).upper().strip()
nome = n1.split()
print('Seja Bem Vindo, Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
