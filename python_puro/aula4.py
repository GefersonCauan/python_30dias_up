# ------------------------------
# Sistema de Notas (várias matérias)
# ------------------------------

materias = ["Matemática", "Português", "História", "Ciências"]
notas = []  # lista onde vamos guardar as notas

print("Digite as notas de cada matéria (0 a 10):\n")

# coleta de notas
for materia in materias:
    nota = float(input(f"{materia}: "))
    notas.append(nota)

# cálculo da média
soma = sum(notas)  # soma todos os valores da lista
media = soma / len(notas)

print("\n--- RESULTADO FINAL ---")
print(f"Notas: {notas}")
print(f"Média final: {media:.2f}")

# classificação
if media >= 7:
    print("✅ Você foi APROVADO!")
elif media >= 5:
    print("⚠️ Você está em RECUPERAÇÃO.")
else:
    print("❌ Você foi REPROVADO!")
