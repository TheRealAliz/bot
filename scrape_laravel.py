import requests
import os

def scrape_laravel():
    """Fetch laravel.com and save just the HTML"""
    
    print("🌐 Fetching laravel.com...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get('https://laravel.com', headers=headers)
    
    if response.status_code == 200:
        # Save HTML file
        with open('laravel.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        file_size = len(response.text)
        print(f"✅ Saved laravel.html ({file_size} characters)")
        return True
    else:
        print(f"❌ Failed: {response.status_code}")
        return False

if __name__ == "__main__":
    scrape_laravel()
