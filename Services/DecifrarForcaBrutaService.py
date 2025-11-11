from Services.Deslocar import deslocar
import requests

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