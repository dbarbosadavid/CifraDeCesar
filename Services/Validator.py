from Models.Alfabeto import Alfabeto
from fastapi import HTTPException

def validar(texto: str, deslocamento: int):
    if deslocamento <= 0:
        raise HTTPException(status_code=406, detail="O deslocamento deve ser maior que 0")
    elif deslocamento % 26 == 0:
        raise HTTPException(status_code=406, detail="O deslocamento não pode ser múltiplo de 26")

    if len(texto) < 3:
        raise HTTPException(status_code=406, detail="O texto deve conter, no mínimo, 3 caracteres")

    for char in texto:
        if not char in Alfabeto().get():
            raise HTTPException(status_code=406, detail="Apenas caracteres de (a-z) e espaços são aceitos!")

    deslocamento = deslocamento % 26
    return texto, deslocamento




