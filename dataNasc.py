data = input('Digite a sua data de nascimento dd/mm/aaaa: ')
data = data.split('/')
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
m = int(data[1])
m = m-1
print('Você nasceu em {} de {} de {}'.format(data[0], mes[m], data[2]))



