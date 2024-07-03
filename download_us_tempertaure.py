import os
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/"

# Directory to save downloaded files
download_dir = "us_temperature_data"

# Ensure download directory exists
os.makedirs(download_dir, exist_ok=True)

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def get_file_links(year):
    url = f"{base_url}{year}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = []
    for link in soup.find_all('a'):
        file_name = link.get('href')
        if file_name.endswith('.txt'):
            links.append(f"{url}{file_name}")
    
    return links

def main(fresh_data=False, max_year=2001):
    if fresh_data:
        for year in range(2000, max_year+1):
            print(f"Processing year: {year}")
            file_links = get_file_links(year)
            for file_url in file_links:
                file_name = file_url.split('/')[-1]
                save_path = os.path.join(download_dir, file_name)
                print(f"Downloading {file_url} to {save_path}")
                download_file(file_url, save_path)
        print("Download complete.")
    else:
        if not os.listdir(download_dir):
            print('No data exist, consider re-run with fresh_data=True to download data from server')
        else:
            print(f"{len(os.listdir(download_dir))} files in folder. For new data re-reun with fresh_data=True")

if __name__ == "__main__":
    main(fresh_data=False, max_year=2024)
