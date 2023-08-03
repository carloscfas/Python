dis = float(input('Qual foi a distancia percorrida em Km? '))
if dis <= 200:
    preço = dis * 0.5
else:
    preço = dis * 0.45
print(f'E o preço da sua passagem será de RS{preço}')
