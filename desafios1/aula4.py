# O Plano de Internet
# Pede quantos GB o usuário consome por mês.
# até 10 GB → “Plano Básico”
# até 30 GB → “Plano Intermediário”
# acima de 30 GB → “Plano Premium”
# 👉 foco: condições com prioridade

gb = float(input("Quantos Gb voçe consome no mês: "))

if gb <= 10:
    print("Plano basico!")
elif gb <= 30:
    print("Plano intermediario")
elif gb > 30:
    print("Plano premium") 