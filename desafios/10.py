#desafio 10
#
#(nome=str(input('qual seu nome? '))
#if nome=='Edson':
#   print('Que nome lindo você tem!  ')
#else:
#   print('Seu nome é tão normal! ')
#    print('bom dia, {}! '.format(nome))

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#considere US$1,00 = R$3,27

real=float(input('Quanto de dinheiro você tem na carteira R$ '))
dolar=real/5.17
E=real/5.14
print('Considerando o valor R$ {:.2f} você pode comprar  US$ {:.2f} ,€$ {:.2f} '.format(real,dolar,E))


