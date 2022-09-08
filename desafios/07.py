#desafio 07
#Desenvolva um programa que leia as duas notas de um aluno,calcule e mostre sua média.

n1=int(input('digite a primeira nota  '))
n2=int(input('digite a segunda nota  '))

print(' 1º nota {:.1f}, 2º nota {:.1f},resultado é {:.1f}.'.format(n1,n2,((n1+n2)/2)))
