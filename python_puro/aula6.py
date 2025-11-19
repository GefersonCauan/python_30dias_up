# Faça um programa para uma loja de tintas do programa deverá pedir o tamanho em metros quadrados da área a ser pintado Ok Considero que a cobertura de tinta é de 1 litro para cada 3 m² e o que a tinta é vendida em latas de 18 L que custa r$ 80 e forme ao usuário a quantidade de latas de tinta a serem compradas e o preço tinta.
CUSTO_TOTAL = 80

metros_quadrado = int(input("Digite a quantidade de  metros: "))

litros, resto = divmod(metros_quadrado, 3)

if resto > 0:
    litros += 1

latas, adicional = divmod(litros, 18) 

if adicional > 0:
    latas += 1

custo = latas * CUSTO_TOTAL

print("a quantidade de latas de tinta: ", latas)
print(f"o valor total R${custo}")