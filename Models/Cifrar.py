from pydantic import BaseModel, Field

class CifrarRequest(BaseModel):
    textoClaro: str = Field(
        description="Texto a ser cifrado",
        examples=["ola pessoal"])

    deslocamento: int = Field(
        description="Deslocamento a ser feito pela cifra de césar",
        examples=[3])

class CifrarResponse(BaseModel):
    textoCifrado: str = Field(
        description="Texto cifrado",
        examples=["rod shvvrdo"])

