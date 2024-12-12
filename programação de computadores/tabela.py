def natural_para_binario(n):
    # Converte um número natural para binário com 12 bits
    return bin(n)[2:].zfill(12)

def binario_para_natural(b):
    # Converte binário para número natural
    return int(b, 2)

def soma_magnitude_para_decimal(binario):
    """
    Converte um número binário para o formato de soma de magnitudes:
    - Se o número binário começa com 1, trata-se de um número negativo.
    - Se o número binário começa com 0, é um número positivo.
    """
    # Verifica se o número é negativo (começa com '1')
    if binario[0] == '1':
        # Número negativo: converte os bits restantes para decimal e coloca o sinal negativo
        valor = int(binario[1:], 2)  # Converte os bits restantes (sem o primeiro '1') para decimal
        return -valor
    else:
        # Número positivo: converte diretamente para decimal
        return int(binario, 2)
def complemento_2_para_decimal(binario):
    """
    Converte um número binário em complemento de 2 para decimal.
    - Se o número binário começa com 1, inverte os bits e soma 1 antes de converter para decimal.
    - Se o número binário começa com 0, converte diretamente para decimal.
    """
    # Verifica se o número é negativo (começa com '1')
    if binario[0] == '1':
        # Inverte os bits
        invertido = ''.join('1' if bit == '0' else '0' for bit in binario[1:])
        
        # Soma 1 ao número invertido
        binario_invertido_soma_1 = bin(int(invertido, 2) + 1)[2:].zfill(len(binario) - 1)
        
        # Converte para decimal com o sinal negativo
        return -int(binario_invertido_soma_1, 2)
    else:
        # Número positivo: converte diretamente para decimal
        return int(binario, 2)