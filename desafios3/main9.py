# O Relógio Lógico
# ⏳ Missão:
# Peça a hora atual (ex: 14) e diga:
# “Bom dia” se < 12
# “Boa tarde” se < 18
# “Boa noite” se >= 18
# 💡 Dicas:
# Aqui você treina comparações (<, >=) e blocos if / elif / else.

hora = int(input("Que horas são?"))
if hora < 12:
    print("Bom dia")
elif hora < 18:
    print("Boa tarde")
elif hora >= 18:    
    print("Boa noite")

