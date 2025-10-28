```markdown
# Primeros Libros Scraper

A Python-based web scraper for extracting comprehensive metadata from the Primeros Libros de las Américas digital collection.

## Overview

This tool extracts detailed bibliographic information from the Primeros Libros de las Américas exhibit (https://primeroslibros.org), capturing metadata for 16th-century American printed books including titles, authors, publishers, dates, languages, physical descriptions, and repository information.

## Features

- **Comprehensive Data Extraction**: Captures 23+ metadata fields per book item
- **Local HTML Processing**: Works with saved web pages to avoid server load
- **CSV Export**: Saves structured data in spreadsheet-friendly format
- **Error Handling**: Gracefully handles missing fields and malformed data
- **Unicode Support**: Properly handles special characters and historical typography

## Data Fields Extracted

- **Basic Identification**: Title, URL, Document Counter, Thumbnail URL
- **Title Information**: Alternative titles, subtitles
- **Creator Information**: Authors, contributors, publishers
- **Bibliographic Data**: Publication dates, geographic coverage, languages
- **Physical Description**: Extent, genre, topics
- **Repository Information**: Owning institutions, local identifiers
- **Content**: Descriptions, condition notes, general notes
- **Rights**: License information, citation notes

## Installation

### Prerequisites
- Python 3.6+
- pip (Python package manager)

### Dependencies
```bash
pip install beautifulsoup4 lxml requests
```

Or install all dependencies at once:
```bash
pip install beautifulsoup4 lxml requests && pip freeze > requirements.txt
```

## Usage

### Step 1: Save the Web Page
1. Navigate to: https://primeroslibros.org/spotlight/primeros-libros-de-las-americas/browse/all-exhibit-items
2. Wait for the page to fully load
3. Use "File → Save As → Web Page, Complete" in your browser
4. Save as `primeros_libros.html` (or update the path in the script)

### Step 2: Run the Scraper
```bash
python3 primeros_libros_scraper.py
```

### Step 3: Check Output
- Console output shows progress and sample data
- Full dataset saved as `primeros_libros_data.csv`

## File Structure

```
primeros_libros_scraper/
├── primeros_libros_scraper.py  # Main scraper script
├── primeros_libros.html        # Saved web page (user-provided)
├── primeros_libros_data.csv    # Generated output
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Output

The script generates a CSV file with the following structure:

| Column | Description | Example |
|--------|-------------|---------|
| `title` | Book title | "Confesionario breve, en lengua mexicana y castellana" |
| `url` | Item page URL | "https://primeroslibros.org/spotlight/.../catalog/..." |
| `creator_contributor` | Author/contributor | "Molina, Alonso de, 1514-1585 (author)" |
| `date_created_issued` | Publication date | "1577" |
| `language` | Languages used | "Nahuatl languages\|nah\|Spanish\|spa" |
| ... | ... | ... |

## Ethical Usage

⚠️ **Important Notes:**

- This tool is designed for **research and educational purposes only**
- Always respect `robots.txt` and website terms of service
- The script uses locally saved HTML to minimize server impact
- Consider adding delays if adapting for live scraping
- Check licensing information for each item before reuse
- Credit original institutions when publishing research

## Technical Details

- **Parser**: BeautifulSoup4 with lxml backend for fast HTML parsing
- **Encoding**: UTF-8 for proper handling of historical typography
- **Output**: CSV with proper field quoting and special character handling
- **Compatibility**: Python 3.6+, cross-platform

## Troubleshooting

**Common Issues:**

1. **"File not found"**: Update `file_path` variable in the script
2. **Encoding errors**: Ensure HTML file is saved with UTF-8 encoding
3. **Missing fields**: Some items may not have all metadata fields
4. **Permission errors**: Check file read/write permissions

## License

This scraper tool is provided for academic and research use. The data extracted belongs to the respective cultural heritage institutions. Please respect their licensing and citation requirements.

## Contributing

Feel free to submit issues and enhancement requests for additional features or improved data extraction.