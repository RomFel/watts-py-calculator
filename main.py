aparelhos = []
total = 0

while True:
    aparelho = input('Aparelho: ')
    unidades = input('Unidades:')
    consumo = input('Watts/h: ')
    horas = input('Horas: ')
    dias = input('Dias: ')

    aparelhos.append({'aparelho': aparelho, 'unidades': unidades, 'consumo': consumo, 'horas': horas, 'dias': dias})
    continuar = input('adicionar outro aparelho? [s/n]: ')[0]
    if continuar in 'Nn':
        break

for aparelho in aparelhos:
    aparelho_total = int(aparelho['unidades'])*int(aparelho['consumo'])*int(aparelho['horas'])*int(aparelho['dias'])
    total += aparelho_total
    print()
    print(f'Aparelho: {aparelho['aparelho']}\n'
          f'Consumo: {aparelho['consumo']} watts/h\n'
          f'Horas: {aparelho['horas']} | Dias: {aparelho['dias']}\n'
          f'Total: {aparelho_total} watts/h')
    print()
print('-'*30)
print(f'Total: {total/1000} kW/h')
tarifa = float(input('Informe as tarifas da sua conta (TE+TUSD): '))
print(f'R$: {(total/1000)*tarifa}')