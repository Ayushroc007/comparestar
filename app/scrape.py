import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_site_1(product):
    url = f"https://example-site-1.com/search?q={product}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    prices = [float(div.text.split('$')[1]) for div in soup.find_all('div', class_='price')]
    return prices

def scrape_site_2(product):
    url = f"https://example-site-2.com/products?search={product}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    prices = [float(span.text.replace('$', '')) for span in soup.find_all('span', class_='product-price')]
    return prices

def compare_prices(product):
    prices_site_1 = scrape_site_1(product)
    prices_site_2 = scrape_site_2(product)
    
    data = {
        'Site': ['Site 1'] * len(prices_site_1) + ['Site 2'] * len(prices_site_2),
        'Price': prices_site_1 + prices_site_2
    }
    
    df = pd.DataFrame(data)
    return df

