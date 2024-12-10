
# Competitor Analysis Tool

The **Competitor Analysis Tool** is a Python-based script designed to scrape competitor websites for SEO-related information such as keywords, meta tags, and other relevant data. This tool helps you analyze your competitors' web presence and optimize your own website accordingly.

## Features

- Extracts the following SEO-related information from competitor websites:
  - Page Title
  - Meta Description
  - Meta Keywords
  - H1 Tags
  - Canonical Tag
- Saves the extracted data into a CSV file for easy analysis.

## Requirements

- Python 3.x
- Libraries: `requests`, `beautifulsoup4`, `pandas`

## Installation

Follow these steps to set up the project:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd competitor_analysis
   ```

2. **Ensure you have Python installed**. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install the required libraries** using pip:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

## Usage

1. **Create a text file** named `urls.txt` in the project directory. Add the competitor URLs you want to analyze, one per line:
   ```
   https://www.example.com
   https://www.example.org
   ```

2. **Run the script**:
   ```bash
   python competitor_analysis.py
   ```

3. After execution, check `output_meta_data.csv` for the extracted SEO-related information.

## Example Output

The generated `output_meta_data.csv` will contain columns for:
- URL
- Title
- Meta Description
- Meta Keywords
- H1 Tags
- Canonical Tag

### Sample Output:

```csv
URL,Title,Meta Description,Meta Keywords,H1 Tags,Canonical Tag
https://www.example.com,"Example Title","This is an example description.","keyword1, keyword2","['H1 Tag 1']",https://www.example.com/page/
https://www.example.org,"Another Example Title","Another example description.","keyword3, keyword4","['H1 Tag 2']",https://www.example.org/page/
```

## Known Issues

- Ensure that the URLs provided in `urls.txt` are accessible and return valid responses (HTTP status code 200).
- The script may not work correctly if the structure of the target websites changes.

## Future Improvements

- Enhance error handling for better user feedback.
- Add support for scraping additional SEO metrics such as backlinks or social media presence.
- Implement a graphical user interface (GUI) for easier use.

## License

This project is open-source and available under the MIT License.

