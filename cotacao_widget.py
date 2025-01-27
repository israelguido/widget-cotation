import requests

def obter_cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        
        usd_brl = dados['USDBRL']
        eur_brl = dados['EURBRL']
        btc_brl = dados['BTCBRL']

        # Escreve as cotações em um arquivo
        with open("/tmp/cotacoes.txt", "w") as arquivo:
            arquivo.write("Cotação Atual:\n")
            arquivo.write(f"Dólar (USD-BRL): R$ {usd_brl['bid']}\n")
            arquivo.write(f"Euro (EUR-BRL): R$ {eur_brl['bid']}\n")
            arquivo.write(f"Bitcoin (BTC-BRL): R$ {btc_brl['bid']}\n")
    except requests.exceptions.RequestException as e:
        with open("/tmp/cotacoes.txt", "w") as arquivo:
            arquivo.write(f"Erro ao acessar a API: {e}")

if __name__ == "__main__":
    obter_cotacoes()
