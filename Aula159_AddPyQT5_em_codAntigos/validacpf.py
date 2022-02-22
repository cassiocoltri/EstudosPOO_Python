import re


def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)  # Essa cunf re.SUB esta subistituindo TUDO o que não for 0-9 por nada

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]  # Elimina os dois ultimos digitos do CPF
    reverso = 10  # Contador reverso.
    total = 0

    # Loop CPF
    for index in range(19):
        if index > 8:  # Primeiro indice vai de 0 a 9
            index -= 9  # São os 9 primeiros digitos CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1  # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:  # Se o digito for > 9 o valor é 0
                d = 0
            total = 0  # Zera o total.
            novo_cpf += str(d)  # Concatena o digito gerado no novo CPF

    # Evita sequencias. Ex: 00000000000000 e 111111111111111...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequencia avaliam como verdadeiro, entao também adicionei essa checagem aqui:
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False
