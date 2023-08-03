perg = float(input('Qual foi a sua velocidade na via Dutra? '))
velo = perg - 80
multa = velo * 7
if perg <= 80:
    print('Fique Tranquilo, Andou sobre o Esperado da via 80Km/h!')
else:
    print(f'Vocẽ ultrapassou a velocidade da via 80Km/h, e será multado em {multa} Reais por cada Km/h ultrapassado! ')
