# Widget de Cotações para Área de Trabalho no Manjaro/Linux

Este tutorial descreve como criar um widget para exibir cotações do dólar, euro e bitcoin diretamente na área de trabalho do Manjaro usando **Python** e **Conky**.

![Captura de tela de 2025-01-27 11-44-24](https://github.com/user-attachments/assets/ffc78aee-8b7c-4689-b94b-cbf99837f47f)


---

## Pré-requisitos

- Python 3 instalado
- Gerenciador de pacotes `pip`
- Conky instalado no sistema

---

## 1. Instale o Conky

No Manjaro, instale o Conky com o comando:

```bash
sudo pacman -S conky
```

---

## 2. Crie o Script Python

Crie um arquivo chamado `cotacao_widget.py` e cole o código abaixo:

```python
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
```

Salve o arquivo em um local de sua preferência, por exemplo, em `~/scripts/cotacao_widget.py`.

---

## 3. Agende o Script para Rodar Periodicamente

Para atualizar as cotações automaticamente, configure o `cron`:

1. Edite o crontab com o comando:

   ```bash
   crontab -e
   ```

2. Adicione a seguinte linha para executar o script a cada 5 minutos:

   ```bash
   */5 * * * * python /caminho/para/cotacao_widget.py
   ```

Substitua `/caminho/para/cotacao_widget.py` pelo caminho completo para o arquivo.

---

## 4. Configure o Conky

Crie ou edite o arquivo de configuração do Conky, normalmente localizado em `~/.conkyrc`. Cole o seguinte conteúdo:

```lua
conky.config = {
    -- Define o alinhamento do widget na tela. 'top_right' posiciona-o no canto superior direito.
    alignment = 'top_right',

    -- Torna o widget visível no fundo da área de trabalho.
    background = true,

    -- Intervalo de atualização do Conky em segundos. 
    update_interval = 1.0,

    -- Habilita o uso de buffer duplo para evitar artefatos visuais.
    double_buffer = true,

    -- Habilita uma janela própria para o Conky, garantindo que ele não se misture com outros aplicativos.
    own_window = true,

    -- Define o tipo de janela como 'desktop', para que ela fique integrada à área de trabalho.
    own_window_type = 'desktop',

    -- Torna a janela transparente.
    own_window_transparent = true,

    -- Define dicas para a janela, como ausência de decoração, abaixo de outras janelas, fixo e sem aparecer na barra de tarefas ou no pager.
    own_window_hints = 'undecorated,below,sticky,skip_taskbar,skip_pager',

    -- Largura mínima da janela do Conky.
    minimum_width = 200,

    -- Altura mínima da janela do Conky.
    minimum_height = 100,

    -- Ativa o uso de fontes Xft para uma melhor renderização.
    use_xft = true,

    -- Define a fonte e o tamanho do texto exibido no widget.
    font = 'DejaVu Sans Mono:size=10',

    -- Define a cor padrão do texto.
    default_color = 'white',
};

conky.text = [[
${exec cat /tmp/cotacoes.txt}
]];

```

---

## 5. Inicie o Conky

Para iniciar o Conky e exibir o widget, use o comando:

```bash
conky
```

---

## 6. Adicione o Conky à Inicialização do Sistema

Para iniciar o Conky automaticamente com o sistema:

1. Abra o gerenciador de inicialização da sua interface gráfica (KDE, XFCE, GNOME, etc.).
2. Adicione um novo item de inicialização com o comando:

   ```bash
   conky &
   ```

---

Agora, você terá um widget funcional na sua área de trabalho exibindo as cotações de dólar, euro e bitcoin! 🎉
