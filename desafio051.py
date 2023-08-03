print('=' * 25)
print('10 TERMOS DE UMA PA')
print('=' * 25)
pri = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
de = pri + (10 - 1) * ra
for c in range(pri, de + ra, ra):
    print(c, end=' → ')
print('ACABOU')