#Faça umm programa que leia a largura e a altura de uma parede em metros, calcule  a sua area e a quantidade de tinta necessária  para pintala, sabendo que cada litro de tinta pinta uma area de dois metros quadrados.
largura = float(input("Digite a largura da parede:"))
altura = float(input("Digite a altura da parede:"))
area = altura*largura

print('A área é : {}m²'.format(area))
print('A tinta necessária para pintar a parede é de {} litros'.format(area//2+1))

