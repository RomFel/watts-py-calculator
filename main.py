aparelhos = []

while True:
    aparelho = input('Aparelho: ')
    consumo = input('Watts/h: ')
    horas = input('Horas: ')
    dias = input('Dias: ')

    aparelhos.append({'aparelho': aparelho, 'consumo': consumo, 'horas': horas, 'dias': dias})
    continuar = input('adicionar outro aparelho? [s/n]: ')[0]
    if continuar in 'Nn':
        break

print(aparelhos)

for aparelho in aparelhos:
    print()
    print(f'Aparelho: {aparelho['aparelho']}\n'
          f'Consumo: {aparelho['consumo']} watts/h\n'
          f'Horas: {aparelho['horas']}\n'
          f'Dias: {aparelho['dias']}')
    print()
    