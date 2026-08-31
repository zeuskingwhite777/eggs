import requests
import json
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def consultar_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return {"erro": "CNPJ não encontrado ou inválido"}
    except:
        return {"erro": "Erro na conexão com a API"}

def consultar_cep(cep):
    cep = ''.join(filter(str.isdigit, cep))
    url = f"https://brasilapi.com.br/api/cep/v2/{cep}"
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return {"erro": "CEP não encontrado ou inválido"}
    except:
        return {"erro": "Erro na conexão com a API"}

def consultar_ddd(ddd):
    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return {"erro": "DDD não encontrado ou inválido"}
    except:
        return {"erro": "Erro na conexão com a API"}

def consultar_telefone(numero):
    # API gratuita com limite de 100 consultas/mês
    api_key = "a7e8b2753c20c5e1cb5b1e0a4ba5fc81"  # Pegue em: https://numverify.com/
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={numero}&country_code=BR"
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            dados = resposta.json()
            if dados.get('valid'):
                return dados
            else:
                return {"erro": "Número inválido"}
        else:
            return {"erro": "Erro na API de telefone"}
    except:
        return {"erro": "Erro na conexão"}

def menu():
    while True:
        limpar_tela()
        print("="*50)
        print("   🔍 CONSULTA DE DADOS BRASIL 🇧🇷")
        print("="*50)
        print("1 - Consultar CNPJ")
        print("2 - Consultar CEP")
        print("3 - Consultar DDD")
        print("4 - Consultar Telefone")
        print("5 - Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cnpj = input("Digite o CNPJ: ")
            resultado = consultar_cnpj(cnpj)
            print("\n" + json.dumps(resultado, indent=2, ensure_ascii=False))
            input("\nPressione ENTER para continuar...")
            
        elif opcao == "2":
            cep = input("Digite o CEP: ")
            resultado = consultar_cep(cep)
            print("\n" + json.dumps(resultado, indent=2, ensure_ascii=False))
            input("\nPressione ENTER para continuar...")
            
        elif opcao == "3":
            ddd = input("Digite o DDD: ")
            resultado = consultar_ddd(ddd)
            print("\n" + json.dumps(resultado, indent=2, ensure_ascii=False))
            input("\nPressione ENTER para continuar...")
            
        elif opcao == "4":
            telefone = input("Digite o telefone (com DDD): ")
            resultado = consultar_telefone(telefone)
            print("\n" + json.dumps(resultado, indent=2, ensure_ascii=False))
            input("\nPressione ENTER para continuar...")
            
        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida!")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    menu()