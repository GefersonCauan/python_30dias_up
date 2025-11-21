def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica tamanho
    if len(cpf) != 11:
        return False

    # Elimina CPFs como 11111111111
    if cpf == cpf[0] * 11:
        return False

    # Calcula o 1º dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    primeiro_digito = (soma * 10) % 11
    if primeiro_digito == 10:
        primeiro_digito = 0

    if primeiro_digito != int(cpf[9]):
        return False

    # Calcula o 2º dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    segundo_digito = (soma * 10) % 11
    if segundo_digito == 10:
        segundo_digito = 0

    if segundo_digito != int(cpf[10]):
        return False

    return True

print(validar_cpf("123.456.789-09"))  # Exemplo de uso