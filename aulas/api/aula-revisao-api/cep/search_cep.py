import urllib.request
import json

def search_addres(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read()
                address = json.loads(data)

                street = address["logradouro"]
                city = address["localidade"]
                state = address["uf"]

                print(f"Rua: {street}")
                print(f"Cidade: {city} - {state}")
            else:
                print("Resposta com erro")
    except:
        print("Erro na solicitação")


cep_input = input("Digite o CEP: ")
search_addres(cep_input)