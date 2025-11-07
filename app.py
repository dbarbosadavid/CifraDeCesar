from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from models import CifrarBodyRequest, CifrarBodyResponse, DecifrarBodyRequest, DecifrarBodyResponse, DecifrarForcaBrutaRequest, DecifrarForcaBrutaResponse, Alfabeto
import requests

app = FastAPI(
    title="Cifra de César: API",
    openapi_url="/cifra-de-cesar",
    description="Esta API cifra e decifra textos com a Cifra de César."
    )


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"mensagem": f"ERRO! {exc.detail}"},
    )

@app.post("/cifrar", 
          response_model=CifrarBodyResponse)

def cifrar(cifrarBody: CifrarBodyRequest):
    textoClaro = cifrarBody.textoClaro
    deslocamento = cifrarBody.deslocamento

    textoClaro, deslocamento = verificar(textoClaro, deslocamento)
    
    textoCifrado = deslocar(textoClaro, deslocamento, 'cifrar')

    response = CifrarBodyResponse(textoCifrado=textoCifrado)

    return response


@app.post("/decifrar", 
          response_model=DecifrarBodyResponse)
def decifrar(decifrarBody: DecifrarBodyRequest):
    textoCifrado = decifrarBody.textoCifrado
    deslocamento = decifrarBody.deslocamento

    textoClaro, deslocamento = verificar(textoCifrado, deslocamento)
    textoClaro = deslocar(textoClaro, deslocamento, 'decifrar')

    response = DecifrarBodyResponse(textoClaro=textoClaro)
    return response

@app.post("/decifrarForcaBruta", 
          response_model=DecifrarForcaBrutaResponse)
def decifrar(decifrarForcaBrutaBody: DecifrarForcaBrutaRequest):
    textoCifrado = decifrarForcaBrutaBody.textoCifrado

    textoClaro, deslocamento = verificar(textoCifrado, 1)

    textoClaro = decifrarForcaBruta(textoCifrado)
    response = DecifrarBodyResponse(textoClaro=textoClaro)

    return response


def deslocar(
        texto: str, 
        deslocamento: int,
        call: str
    ):
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


def verificar(texto:str, deslocamento: int):
    if deslocamento <= 0:
        raise HTTPException(status_code=406, detail="O deslocamento deve ser maior que 0")
    elif deslocamento % 26 == 0:
        raise HTTPException(status_code=406, detail="O deslocamento não pode ser múltiplo de 26")
    
    if len(texto) < 3:
        raise HTTPException(status_code=406, detail="O texto deve conter mais de 3 caracteres")
    
    for char in texto:
        print(Alfabeto().get())
        if not char in Alfabeto().get():
            raise HTTPException(status_code=406, detail="Não são aceitos caracteres especiais")
    
    texto = texto.lower()

    deslocamento = deslocamento % 26
    return texto, deslocamento

def decifrarForcaBruta(textoCifrado: str):
    
    url = 'https://www.dicio.com.br/'
    dict = {}
    for i in range(25):
        textoClaro = deslocar(texto=textoCifrado, deslocamento=i, call='decifrar')
        print(textoClaro)
        texto = textoClaro.split(' ')
        for palavra in texto:
            response = requests.get(url + palavra)
            if response.status_code == 200:
                if i in dict.keys():
                    dict[i] += 1
                else:
                    dict[i] = 1
            
    dict = {chave: valor for chave, valor in dict.items() if valor >= 1}
    dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    
    if len(dict) > 0: 
        deslocamento = dict[0][0] 
    else:
        raise HTTPException(status_code=406, detail="Não foi possível decifrar o texto")

    texto = deslocar(texto=textoCifrado, deslocamento=deslocamento, call='decifrar')
    return texto




