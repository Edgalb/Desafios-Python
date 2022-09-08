#desafio 08
#Escreva um programa que leia um valor em metros e a exiba convertida em centimetros e milímetros.

# KM hm dam m dm cm mm

medida = float(input('uma distancia em metros '))
cm= medida*100
mm= medida*1000
print('A medida {}m corresponde a {}cm e {}mm'.format(medida,cm,mm))
