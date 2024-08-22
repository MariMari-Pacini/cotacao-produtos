import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import schedule
import time
import os

def fetch_product_price(url, selector):
    """Obtém o preço do produto a partir da URL usando BeautifulSoup."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve um erro na requisição
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.select_one(selector)
        if price_element:
            return price_element.get('content', '').replace(',', '.')
        else:
            print("Elemento de preço não encontrado.")
            return None
    except requests.RequestException as e:
        print(f'Erro ao acessar o site: {e}')
        return None

def save_to_excel(data, filename):
    """Salva os dados em uma planilha Excel usando pandas."""
    if os.path.exists(filename):
        df = pd.read_excel(filename)
        # Usa o pd.concat em vez de append
        df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)
    else:
        df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def job():
    """Função a ser executada periodicamente."""
    url = 'https://www.mercadolivre.com.br/notebook-positivo-vision-r15-lumina-bar-amd-ryzen-5-8gb-256gb-tela-15-polegadas-full-hd-antirreflexo-windows-11-home-tecla-copilot-preto/p/MLB37293576#searchVariation%3DMLB37293576%26position%3D3%26search_layout%3Dgrid%26type%3Dproduct%26tracking_id%3D2bcee364-d363-4a21-8d91-6b9d57785dbb'
    selector = 'meta[itemprop="price"]'  # Ajuste conforme necessário
    price_value = fetch_product_price(url, selector)
    
    if price_value:
        try:
            price = float(price_value)
        except ValueError:
            print("Valor do preço não é um número válido.")
            return

        product_data = [{
            'Produto': 'Notebook Positivo Vision R15',
            'Data': datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S'),
            'Preco': price,
            'Link': url
        }]
        
        save_to_excel(product_data, 'product_prices.xlsx')
        print('Dados salvos com sucesso.')

def notify_user():
    """Notifica o usuário após a execução da tarefa."""
    print("O tracker foi executado e os dados foram salvos com sucesso! Proxima cotacao daqui 30 minutos.")

def main():
    # Executa a tarefa imediatamente ao iniciar o script
    job()
    
    # Agenda a tarefa para rodar a cada 30 minutos
    schedule.every(30).minutes.do(job)
    schedule.every(30).minutes.do(notify_user)

    print("Agendamento de cotacao iniciado para cada 30 minutos. Pressione Ctrl+C para sair.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
