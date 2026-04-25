# quick_scrape.py
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path

def quick_scrape():
    # Setup
    os.makedirs("laravel_page", exist_ok=True)
    
    # Get page
    print("Fetching laravel.com...")
    response = requests.get('https://laravel.com', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Save HTML
    with open('laravel_page/index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    # Save to a single file
    with open('laravel_page/full_page.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    print(f"✅ Saved! HTML size: {len(response.text)} characters")
    print(f"📁 Files saved to 'laravel_page/' directory")

if __name__ == "__main__":
    quick_scrape()
