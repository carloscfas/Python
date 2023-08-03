import math
an = int(input('Digite o angulo que voce deseja:' ))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print(f'O angulo de {an} tem o SENO de {seno}')
print(f'O anglo de {an} tem o COSSENO de {cosseno}')
print(f'O angulo de {an} tem a TANGENTE de {tangente}')
