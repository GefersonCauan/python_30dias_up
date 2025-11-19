"""a = [1, 2, 3]
b = a  # b aponta pro mesmo lugar
b.append(4)
b.append(5)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
print(a is b)  # True (mesmo objeto)
"""

import copy

original = [[1, 2], [3, 4]]

# Cópia rasa
shallow = copy.copy(original)
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]] -> mudou também

# Cópia profunda
deep = copy.deepcopy(original)
deep[0][0] = 77
print(original)  # [[99, 2], [3, 4]] -> intacto
print(deep)      # [[77, 2], [3, 4]]
