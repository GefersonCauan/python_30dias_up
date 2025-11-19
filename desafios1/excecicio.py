import copy

produto1 = {"id": 1, "nome": "iphone 12", "preço": 7000}
produto2 = {"id": 2, "nome": "pc-gamer", "preço": 10000}
produto3 = {"id": 3, "nome": "mesa", "preço": 300}

catalogo = [produto1, produto2, produto3]

copia_profunda = copy.deepcopy(catalogo)
copia_profunda[1]["preço"] = 8888

print("Catálogo original depois da deepcopy:", catalogo)
print("Cópia profunda:", copia_profunda)

print("id original[1]:", id(catalogo[1]))
print("id copia_profunda[1]:", id(copia_profunda[1]))
