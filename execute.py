#!/usr/bin/env python3
"""
Primeros Libros Scraper - Extended Version

Dependencies:
- beautifulsoup4: HTML parsing
- lxml: Fast HTML parser  
- requests: HTTP requests (for future live scraping)

Install with:
pip install beautifulsoup4 lxml requests && pip freeze > requirements.txt

Usage:
1. Save the webpage manually (File → Save As → Web Page, Complete)
2. Update the file_path variable below with your HTML file location
3. Run this script: python3 execute.py
"""

from bs4 import BeautifulSoup
import os
import csv

def scrape_saved_html(file_path):
    """Scrape from a saved HTML file - Extended version"""
    
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
            item_data = {}
            
            # Basic item identification
            # Title and URL
            h3 = article.find('h3', class_='index_title document-title-heading col-md-12')
            if h3:
                a_tag = h3.find('a')
                if a_tag:
                    item_data['title'] = a_tag.get_text(strip=True)
                    relative_url = a_tag.get('href', '').strip()
                    # Make URL absolute
                    if relative_url.startswith('/'):
                        item_data['url'] = 'https://primeroslibros.org' + relative_url
                    else:
                        item_data['url'] = relative_url
            
            # Document counter
            counter = article.find('span', class_='document-counter')
            if counter:
                item_data['document_counter'] = counter.get_text(strip=True)
            
            # Thumbnail URL
            thumbnail = article.find('div', class_='document-thumbnail')
            if thumbnail:
                img = thumbnail.find('img')
                if img and img.get('src'):
                    item_data['thumbnail_url'] = img['src']
            
            # Extract all metadata fields from definition list
            metadata_dl = article.find('dl', class_='document-metadata')
            if metadata_dl:
                # Title information
                item_data['alternative_title'] = extract_metadata_field(metadata_dl, 'alternative-title')
                item_data['subtitle'] = extract_metadata_field(metadata_dl, 'subtitle')
                item_data['alternative_subtitle'] = extract_metadata_field(metadata_dl, 'alternative-subtitle')
                
                # Creator/Publisher information
                item_data['creator_contributor'] = extract_metadata_field(metadata_dl, 'creator-contributor')
                item_data['publisher'] = extract_metadata_field(metadata_dl, 'publisher')
                
                # Location and date
                item_data['geographic_coverage'] = extract_metadata_field(metadata_dl, 'geographic-coverage')
                item_data['date_created_issued'] = extract_metadata_field(metadata_dl, 'date-created-date-issued')
                
                # Repository information
                item_data['owning_repository'] = extract_metadata_field(metadata_dl, 'owning-repository')
                item_data['related_resource_host'] = extract_metadata_field(metadata_dl, 'related-resource-host')
                item_data['identifier_local'] = extract_metadata_field(metadata_dl, 'identifier-local')
                
                # Physical description
                item_data['extent'] = extract_metadata_field(metadata_dl, 'extent')
                item_data['language'] = extract_metadata_field(metadata_dl, 'language')
                item_data['genre'] = extract_metadata_field(metadata_dl, 'genre')
                
                # Content information
                item_data['topic'] = extract_metadata_field(metadata_dl, 'topic')
                item_data['description'] = extract_metadata_field(metadata_dl, 'description')
                
                # Additional notes
                item_data['condition_note'] = extract_metadata_field(metadata_dl, 'condition-note')
                item_data['general_note'] = extract_metadata_field(metadata_dl, 'general-note')
                
                # Rights and citation
                item_data['license'] = extract_metadata_field(metadata_dl, 'license')
                item_data['citation_note'] = extract_metadata_field(metadata_dl, 'citation-note')
            
            items_data.append(item_data)
            print(f"Item {i+1}: {item_data.get('title', 'No title')}")
        
        print(f"\nSuccessfully extracted {len(items_data)} items with full metadata")
        return items_data
        
    except Exception as e:
        print(f"Error: {e}")
        return []

def extract_metadata_field(metadata_dl, field_name):
    """Extract a specific metadata field from the definition list"""
    dt = metadata_dl.find('dt', class_=f'blacklight-readonly_{field_name}_tesim')
    if dt:
        dd = dt.find_next_sibling('dd')
        if dd:
            return dd.get_text(strip=True)
    return ""

def save_to_csv(items_data, output_file='primeros_libros_data.csv'):
    """Save the extracted data to a CSV file"""
    if not items_data:
        print("No data to save")
        return
    
    # Get all possible field names from the first item
    fieldnames = set()
    for item in items_data:
        fieldnames.update(item.keys())
    
    fieldnames = sorted(fieldnames)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in items_data:
            writer.writerow(item)
    
    print(f"✅ Data saved to {output_file}")

if __name__ == "__main__":
    # Update this path to where you saved the file
    file_path = "primeros_libros.html"
    data = scrape_saved_html(file_path)
    
    if data:
        print("\n✅ SUCCESS: Extended scraper worked!")
        print(f"First item title: {data[0].get('title', 'No title')}")
        print(f"Extracted {len(data[0])} data fields per item")
        
        # Save to CSV
        save_to_csv(data)
        
        # Show sample of first item's data
        print("\n📊 Sample data from first item:")
        for key, value in list(data[0].items())[:5]:  # Show first 5 fields
            print(f"  {key}: {value[:100]}{'...' if len(str(value)) > 100 else ''}")