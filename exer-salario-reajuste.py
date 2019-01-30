salario = float(input('Digite o seu salário: '))
novoSalario = 0
percentualAumento = 0
valorAumento = 0

if salario <= 280.00:
    percentualAumento = float(0.2)
    valorAumento = salario * percentualAumento
    novoSalario = salario + valorAumento

elif salario <= 700.00:
    percentualAumento = float(0.15)
    valorAumento = salario * percentualAumento
    novoSalario = salario + valorAumento

elif salario <= 1500.00:
    percentualAumento = float(0.1)
    valorAumento = salario * percentualAumento
    novoSalario = salario + valorAumento

else:
    percentualAumento = float(0.05)
    valorAumento = salario * percentualAumento
    novoSalario = salario + valorAumento

print('--------------------------------')
print('Salário antes do reajuste: R${:.2f}'.format(salario))
print('Percentual de aumento: {:.2f}%'.format(percentualAumento*100))
print('O valor do aumento: R${:.2f}'.format(valorAumento))
print('O novo salário é: R${:.2f}'.format(novoSalario))
print('--------------------------------')
