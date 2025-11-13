from Models.Cifrar import CifrarRequest, CifrarResponse
from Models.Decifrar import DecifrarRequest, DecifrarResponse
from Models.DecifrarForcaBrutaModel import DecifrarForcaBrutaResponse
from Services.DecifrarForcaBrutaService import decifrarForcaBruta
from Services.Validator import validar
from Services.Deslocar import deslocar

def response(input):
    if not hasattr(input, 'deslocamento'):
        textoClaro = decifrarForcaBruta(input.textoCifrado)
        validar(input.textoCifrado, 1)
        return DecifrarForcaBrutaResponse(textoClaro=textoClaro)
    else:
        if type(input) == CifrarRequest:
            texto, deslocamento = validar(input.textoClaro, input.deslocamento)
            textoCifrado = deslocar(texto, deslocamento, call='cifrar')
            return  CifrarResponse(textoCifrado=textoCifrado)
        elif type(input) == DecifrarRequest:
            texto, deslocamento = validar(input.textoCifrado, input.deslocamento)
            textoClaro = deslocar(texto, deslocamento, call='decifrar')
            return DecifrarResponse(textoClaro=textoClaro)

