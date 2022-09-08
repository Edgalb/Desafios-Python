#desafio 04
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo #
# e todas as informações possiveis sobre ele

a = input ('digite algo: ')
print('O tipo primitivo desse valor é  ', type(a))
print('Só tem espaços? ', a.isspace()) #a.isspace (representa verdadeiro e falso para espaço)
print('É um número? ', a.isnumeric()) #a.isnumeric (representa verdadeiro e falso para caracteres matemáticos)
print('E alfabetico? ', a.isalpha()) #a.isalpha (representa verdadeiro e falso para alfabeto)
print('É alfanumérico? ',a.isalnum()) #a.isalnum (representa verdadeiro e falso para alfanúmerico)
print('Está em maiúsculas? ',a.isupper())#a.isupper (represenata verdadeiro e falso para letras maiúsculas)
print('Está em minúsculas? ',a.islower())#a.islower (representa verdadeiro e falso para letras minúsculas)
print('Está capitalizada?',a.istitle())# a.istitle (representa verdadeiro e falso para palavras com letras com nome proprio)
