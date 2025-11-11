def deslocar(texto: str, deslocamento: int, call: str):
    if call == 'decifrar':
        deslocamento *= -1

    textoCifrado = ''
    for char in texto:
        if char == ' ':
            textoCifrado += ' '
            continue
        ascii = ord(char)
        ascii += deslocamento
        if ascii > 122:
            ascii -= 26
        if ascii < 97:
            ascii += 26
        textoCifrado += chr(ascii)

    return textoCifrado