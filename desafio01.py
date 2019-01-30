valorHora = float(input('Digite o valor que você ganha por hora?'))
qtdHoras = int(input('Digite quantas por dia você trabalha?'))
salario = float(valorHora*qtdHoras*20)
ir = float(salario * 0.11)
inss = float(salario * 0.08)
sindicato = float(salario * 0.05)
salarioLiquido = float(salario - ir - inss - sindicato)


print('\n----------------------------------')
print('Salário Bruto: {:.2f}'.format(salario))
print('IR: {:.2f}'.format(ir))
print('INSS: {:.2f}'.format(inss))
print('Sindicato: {:.2f}'.format(sindicato))
print('----------------------------------')
print('Salário Liquido: {:.2f}'.format(salarioLiquido))

