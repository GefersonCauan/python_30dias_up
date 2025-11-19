# Pede:
# anos de experiência
# nível de inglês (“básico”, “intermediário”, “avançado”)
# se sabe Python (“sim” ou “não”)
# Regras:
# Se experiência < 1 → “Candidato júnior demais.”
# Se experiência >= 1 e inglês == “avançado” e sabe Python → “Contratado para vaga sênior!”
# Se experiência >= 2 e inglês == “intermediário” → “Aprovado para vaga pleno.”
# Se inglês == “básico” → “Reforce o inglês antes de aplicar novamente.”
# Caso contrário → “Candidato elegível para teste técnico.”
# 👉 Treina: lógica cruzada (and/or) + regras profissiona.

exp = int(input("Anos de experiência: "))
ingles = input("Nivel de ingles (basico ao avançado): ").lower()

sabe_python = input("sabe python (sim ou nao): ").lower() == "sim"

if exp < 1:
    print("Cadidato junior demais. ")
elif exp >= 1 and ingles == "avançado"  and sabe_python:
    print("Contratando para vaga Senior")
elif exp >= 2 and ingles == "intermediario":
    print("aprovado para vaga pleno") 
elif ingles == "basico":
    print("reforce o ingles novamente")
else:
    print("candidato elegivel para teste tecnico")    