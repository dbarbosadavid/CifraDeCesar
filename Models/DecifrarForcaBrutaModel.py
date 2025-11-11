from pydantic import BaseModel, Field

class DecifrarForcaBrutaRequest(BaseModel):
    textoCifrado: str = Field(
        description="Texto a ser decifrado por força bruta",
        examples=["rod shvvrdo"])

class DecifrarForcaBrutaResponse(BaseModel):
    textoClaro: str = Field(
        description="Texto decifrado",
        examples=["ola pessoal"])