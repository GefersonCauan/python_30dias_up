# Qual bebida você quer? chá
# Você quer quente ou gelado? quente
# → "Chá quente é ótimo pra relaxar!"
    
def pedir_bebida():
        bebida = input("Qual bebida você quer? ").strip().lower()
        if bebida in ["chá", "café"]:
            temperatura = input("Você quer quente ou gelado? ").strip().lower()
            if temperatura in ["quente", "gelado"]:
                print(f"{bebida.capitalize()} {temperatura} é ótimo pra relaxar!")
            else:
                print("Opção de temperatura inválida. Por favor, escolha 'quente' ou 'gelado'.")

pedir_bebida()                                    