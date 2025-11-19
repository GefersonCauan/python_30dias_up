# Receber um ano (um número inteiro).
# Verificar se esse ano é bissexto usando as regras:
# Se o ano é divisível por 400 → é bissexto (True).
# Senão, se o ano é divisível por 100 → não é bissexto (False).
# Senão, se o ano é divisível por 4 → é bissexto (True).
# Caso contrário → não é bissexto (False).
# Retornar True ou False (não precisa imprimir, só retornar).
# 👉 Exemplo:
# Entrada: 1990 → Saída: False.
# Entrada: 2000 → Saída: True.

def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
print(is_leap(1990))  # False
print(is_leap(2000))  # True
print(is_leap(2025))  # False