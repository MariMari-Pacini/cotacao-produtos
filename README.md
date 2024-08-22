# Rastreador de Preços de Produto

Este projeto é um script Python que automatiza a coleta de preços de produtos em uma página web específica e armazena essas informações em uma planilha Excel. O script utiliza a biblioteca `requests` para obter o conteúdo da página, `BeautifulSoup` para extrair o preço, `pandas` para manipulação de dados em Excel e `schedule` para agendar a execução periódica da coleta.

## Funcionalidades

- **Extração de Preço:** Extrai o valor do produto a partir de uma página web usando um seletor CSS.
- **Processamento de Dados:** Converte e formata o preço extraído para um valor numérico.
- **Criação e Atualização de Planilha:** Cria ou atualiza uma planilha Excel com os dados coletados, incluindo o nome do produto, data, preço e link da página.
- **Agendamento de Tarefas:** Agenda a execução do script em intervalos regulares (configurado para rodar a cada 30 minutos por padrão).
- **Notificação de Execução:** Notifica o usuário quando o script conclui uma coleta de dados.

## Requisitos

- Python 3.7 ou superior
- requests
- beautifulsoup4
- pandas
- schedule


## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/rastreador-precos.git
    cd rastreador-precos
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Execute o script:**

    ```bash
    python main.py
    ```

    - O script iniciará a coleta de dados e salvará as informações na planilha Excel.
    - A coleta será repetida automaticamente a cada 30 minutos (configurável).
    - Para interromper a execução, pressione `Ctrl+C` (Ctrl e o C em conjunto).

## Configuração

1. **Atualize a URL e o seletor CSS:**
    - No script, ajuste a variável `url` para o produto que deseja monitorar.
    - Atualize o seletor CSS (`selector`) para garantir que o script capture corretamente o preço da página.

2. **Personalização do Intervalo de Execução:**
    - O script está configurado para rodar a cada 30 minutos. Você pode alterar esse intervalo na função `schedule.every()` no arquivo `main.py`.

## Notas

- O script utiliza `BeautifulSoup` para extração de informações. Certifique-se de que o seletor CSS está correto e atualizado para a página que deseja monitorar.
- Certifique-se de que a planilha Excel (`product_prices.xlsx`) não está aberta enquanto o script é executado, para evitar erros de gravação.
- Este script é um exemplo básico e pode ser personalizado para atender necessidades específicas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um _issue_ ou enviar um _pull request_ principalmente para sugerir melhorias.

## Licença

Este projeto está licenciado sob os termos da licença MIT.
