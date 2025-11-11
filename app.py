from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from Models.Cifrar import CifrarRequest, CifrarResponse
from Models.Decifrar import DecifrarRequest, DecifrarResponse
from Models.DecifrarForcaBrutaModel import DecifrarForcaBrutaRequest, DecifrarForcaBrutaResponse
from Services.MiddleWare import response

app = FastAPI(
    title="Cifra de César: API",
    openapi_url="/cifra-de-cesar",
    description="Esta API cifra e decifra textos com a Cifra de César.")

@app.post("/cifrar",response_model=CifrarResponse)
def cifrar(cifrarBody: CifrarRequest):
    return response(cifrarBody)

@app.post("/decifrar", response_model=DecifrarResponse)
def decifrar(decifrarBody: DecifrarRequest):
    return response(decifrarBody)

@app.post("/decifrarForcaBruta", response_model=DecifrarForcaBrutaResponse)
def decifrarForcaBruta(decifrarForcaBrutaBody: DecifrarForcaBrutaRequest):
    return response(decifrarForcaBrutaBody)

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"mensagem": f"ERRO! {exc.detail}"})





