from pydantic import BaseModel, Field

class DecifrarRequest(BaseModel):
    textoCifrado: str = Field(
        description="Texto a ser decifrado",
        examples=["rod shvvrdo"])
    deslocamento: int = Field(
        description="Deslocamento a ser feito pela cifra de césar, de forma reversa para decifrar",
        examples=[3])

class DecifrarResponse(BaseModel):
    textoClaro: str = Field(
        description="Texto decifrado",
        examples=["ola pessoal"])

