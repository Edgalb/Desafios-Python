#desafio 29

#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h,mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input ('A sua velocidade ' ))
#v = velocidade*100
v = velocidade
m=(v-80)*7

if  v>=81:
    print(' Esta multado R$ {} '.format(m,v))
else:
    if v<=80:
        print('Boa viagem, sua velocidade {} km/h'.format(v))
