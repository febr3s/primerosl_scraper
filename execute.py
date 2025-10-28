"""
Primeros Libros Scraper

Dependencies:
- beautifulsoup4: HTML parsing
- lxml: Fast HTML parser  
- requests: HTTP requests (for future live scraping)

Install with:
pip install beautifulsoup4 lxml requests && pip freeze > requirements.txt

Usage:
1. Save the webpage manually (File → Save As → Web Page, Complete)
2. Update the file_path variable below with your HTML file location
3. Run this script: python python3 execute.py
"""

from bs4 import BeautifulSoup
import os

def scrape_saved_html(file_path):
    """Scrape from a saved HTML file"""
    
    if not os.path.exists(file_path):
        print(f"File {file_path} not found!")
        return
    
    try:
        # Read the saved HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(html_content, "lxml")
        
        # Find all article elements
        articles = soup.find_all('article')
        print(f"Found {len(articles)} article elements")
        
        # Extract data from each article
        items_data = []
        for i, article in enumerate(articles):
            # Find the h3 with specified classes
            h3 = article.find('h3', class_='index_title document-title-heading col-md-12')
            
            if h3:
                a_tag = h3.find('a')
                if a_tag:
                    title = a_tag.get_text(strip=True)
                    relative_url = a_tag.get('href', '').strip()
                    
                    # Make URL absolute
                    if relative_url.startswith('/'):
                        full_url = 'https://primeroslibros.org' + relative_url
                    else:
                        full_url = relative_url
                    
                    items_data.append({
                        'title': title,
                        'url': full_url
                    })
                    
                    print(f"Item {i+1}: {title}")
        
        print(f"\nSuccessfully extracted {len(items_data)} items")
        return items_data
        
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    # Update this path to where you saved the file
    file_path = "primeros_libros.html"
    data = scrape_saved_html(file_path)
    
    if data:
        print("\n✅ SUCCESS: Local scraping worked!")
        print(f"First item: {data[0]['title']}")