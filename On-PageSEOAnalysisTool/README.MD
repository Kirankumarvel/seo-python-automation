
# On-Page SEO Analysis Tool

This On-Page SEO Analysis Tool is a Python script that checks various SEO metrics across multiple URLs. It analyzes meta tags, titles, descriptions, and other important SEO factors to help improve website optimization.

## Key Features

- Checks for the presence of robots tags
- Counts words on the page
- Analyzes H1 tags
- Counts total links, internal links, and external links
- Counts total images and identifies images without alt and title attributes
- Analyzes schema data (JSON-LD)
- Checks for hreflang tags
- Logs Open Graph and Twitter Card metadata

## Key Libraries

This project uses the following Python libraries:

- `requests`: For sending HTTP requests to retrieve web pages.
- `beautifulsoup4`: For parsing HTML content and extracting data.
- `pandas`: For handling data and exporting results to CSV files.

## Installation

Follow these steps to set up the project:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd seo_analysis_tool
   ```

2. **Ensure you have Python installed**. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install the required libraries** using pip:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

## Usage

1. **Create a text file** named `urls.txt` in the project directory. Add the URLs you want to analyze, one per line:
   ```
   https://www.example.com
   https://www.example.org
   ```

2. **Run the script**:
   ```bash
   python seo_analysis.py
   ```

3. After execution, check `output_results.csv` for the analysis results and `seo_analysis.log` for detailed logs of the SEO metrics.

## Example Output

The generated `output_results.csv` will contain columns for:
- URL
- Title
- Meta Description
- Meta Keywords
- Robots Tag
- Word Count
- H1 Count
- Total Links
- Internal Links
- External Links
- Total Images
- Images Without Alt
- Images Without Title
- Schema Count
- Hreflang Tags
- Open Graph Tags
- Twitter Card Tags

## Potential Errors

While executing the script, you may encounter the following errors:

1. **HTTP Errors (e.g., 404, 500)**:
   - If a URL is not reachable or returns an error status code, it will be logged in `seo_analysis.log`.

2. **Connection Errors**:
   - Ensure you have an active internet connection. If a URL cannot be reached due to network issues, it will also be logged.

3. **Parsing Errors**:
   - If the HTML structure of a page is unexpected or malformed, some elements may not be found. The script will log these occurrences.

4. **File Not Found Error**:
   - Ensure that `urls.txt` exists in the same directory as `seo_analysis.py`. If not found, you will receive an error.

## License

This project is open-source and available under the MIT License.
```

You can update your `README.md` file with the above content to include the detailed instructions and information about the On-Page SEO Analysis Tool.
