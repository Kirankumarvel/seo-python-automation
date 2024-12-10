# Backlink Monitoring System

This Backlink Monitoring System is a Python-based tool designed to monitor backlinks and track their status over time. The tool checks if backlinks are indexed, retrieves important SEO metrics such as Domain Authority, Page Authority, and Spam Score, and saves the results in a CSV file.

## Features

- **Check Backlink Status**: Determine if a backlink is indexed or marked as noindex.
- **SEO Metrics**: Retrieve Domain Authority, Page Authority, and Spam Score using the Moz API.
- **Data Output**: Save results in a CSV file for easy analysis and tracking.

## Requirements

- Python 3.x
- Libraries: `requests`, `beautifulsoup4`, `pandas`

## Installation

Follow these steps to set up the project:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd backlink_monitoring
   ```

2. **Ensure you have Python installed**. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install the required libraries** using pip:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

4. **Set Up Moz API Credentials**:
   - Sign up for an account at [Moz](https://moz.com/) to obtain your access credentials.
   - Replace `'your_access_id'` and `'your_secret_key'` in `backlink_monitor.py` with your actual Moz API credentials.

## Usage

1. **Create a text file** named `urls.txt` in the project directory. Add the backlinks you want to monitor, one per line:
   ```
   https://www.example.com
   https://www.example.org
   ```

2. **Run the script**:
   ```bash
   python backlink_monitor.py
   ```

3. After execution, check `output_results.csv` for the analysis results.

## Example Output

The generated `output_results.csv` will contain columns for:
- Backlink
- Status (Indexed or Noindex)
- Response Code (HTTP status code)
- Domain Authority
- Page Authority
- Spam Score

### Sample Output:

```csv
Backlink,Status,Response Code,Domain Authority,Page Authority,Spam Score
https://www.example.com,Indexed,200,45,30,5
https://www.example.org,noindex,200,50,35,10
```

## Known Issues

- Ensure that your Moz API credentials are valid; otherwise, you may not retrieve metrics.
- The script may fail if the provided URLs are unreachable or do not respond.

## Future Improvements

- Implement scheduling for regular monitoring of backlinks.
- Add notifications (e.g., email alerts) for changes in backlink status.
- Enhance error handling for better user feedback.

## License

This project is open-source and available under the MIT License.
