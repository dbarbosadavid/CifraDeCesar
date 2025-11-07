from pydantic import BaseModel, Field

class CifrarBodyRequest(BaseModel):
    textoClaro: str = Field(
        description="Texto a ser cifrado",
        examples=[
            "ola pessoal"
        ]
    )
    deslocamento: int = Field(
        description="Deslocamento a ser feito pela cifra de césar",
        examples=[
            3
        ]
    )

class CifrarBodyResponse(BaseModel):
    textoCifrado: str = Field(
        description="Texto cifrado",
        examples=[
            "rod shvvrdo"
        ]
    )

class DecifrarBodyRequest(BaseModel):
    textoCifrado: str = Field(
        description="Texto a ser decifrado",
        examples=[
            "rod shvvrdo"
        ]
    )
    deslocamento: int = Field(
        description="Deslocamento a ser feito pela cifra de césar, de forma reversa para decifrar",
        examples=[
            3
        ]
    )

class DecifrarBodyResponse(BaseModel):
    textoClaro: str = Field(
        description="Texto decifrado",
        examples=[
            "ola pessoal"
        ]
    )

class DecifrarForcaBrutaRequest(BaseModel):
    textoCifrado: str  = Field(
        description="Texto a ser decifrado por força bruta",
        examples=[
            "rod shvvrdo"
        ]
    )

class DecifrarForcaBrutaResponse(BaseModel):
    textoClaro: str = Field(
        description="Texto decifrado",
        examples=[
            "ola pessoal"
        ]
    )
    
class Alfabeto():
    def get(self):
        alfabeto = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, x, w, y, z,  '
        alfabeto = alfabeto.split(', ')
        return alfabeto