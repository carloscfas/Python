from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {atual}')
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Ainda faltam {saldo} anos para o alistamento")
    ano = atual + saldo
    print(f'Seu alistamento seŕa em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f"Você já deveria ter se alistado há {saldo} anos")
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
