# 4. Sistema Tributário Nacional
# Pede:
# faturamento anual
# tipo de empresa (“MEI”, “Ltda”, “S/A”)
# Regras:
# MEI: limite 81 mil → 5% imposto
# Ltda: até 4.8 milhões → 10% imposto
# S/A: acima de 4.8 milhões → 15% imposto
# se ultrapassar limite da categoria → alerta “Precisa mudar de regime!”
# Calcule o imposto e mostre lucro líquido (faturamento - imposto).
# 👉 Treina: condições encadeadas + cálculos dinâmicos + validação de regra empresarial

faturamento = float(input("Faturamento anual: "))
tipo_empresa = input("Tipo de empresa (MEI, LTDA, S/A): ").upper()
imposto = 0

if tipo_empresa == "MEI":
    if faturamento <= 81000:
        imposto = faturamento * 0.05
    else:
        print("⚠️ Precisa mudar de regime (ultrapassou o limite do MEI)!")
        imposto = faturamento * 0.05

elif tipo_empresa == "LTDA":
    if faturamento <= 4800000:
        imposto = faturamento * 0.10
    else:
        print("⚠️ Precisa mudar de regime (ultrapassou o limite da LTDA)!")
        imposto = faturamento * 0.10

elif tipo_empresa == "S/A":
    if faturamento > 4800000:
        imposto = faturamento * 0.15
    else:
        print("⚠️ Receita abaixo do esperado para uma S/A!")
        imposto = faturamento * 0.15

else:
    print("Tipo de empresa inválido!")
    imposto = 0

lucro_liquido = faturamento - imposto
print(f"\n💰 Imposto a pagar: R${imposto:,.2f}")
print(f"💼 Lucro líquido: R${lucro_liquido:,.2f}")