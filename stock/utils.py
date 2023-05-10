import requests

def get_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=compact&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    # Aquí puedes procesar y reformatear los datos según lo requieras
    return data
