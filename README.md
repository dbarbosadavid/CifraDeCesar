# API - Cifra de Cesar

Documentação disponível em https://cifradecesar-six.vercel.app/docs

## Este projeto se trata de uma API com três endpoints:

* /cifrar (permite a codificação de um texto através de um deslocamento com base na cifra de cesar)

* /decifrar (permite a decodificação de um texto através de um deslocamento com base na cifra de cesar)

* /decifrarForcaBruta (permite a decodificação de um texto através testando todas as possibilidades, validando os retornos por uma API de dicionário)


# Linguagens/Bibliotecas usadas

* Python 3.13
* FastAPI
* PyDantic
* uvicorn
* requests

# Como rodar

* Instalar Python 3.13 ou superior
* Clonar o repositório
* Instalar as Bibliotecas: 

```
    py -m pip install fastapi pydantic uvicorn requests
```

* Executar comando para rodar o servidor:
```
    py -m uvicorn app:app --reload
```

#### A API já estará rodando, para acessar a documentação e testar os endpints:

* No navgeador, basta acessar:
```
    127.0.0.1:8000/docs
```


# Projeto elaborado para fins acadêmicos
