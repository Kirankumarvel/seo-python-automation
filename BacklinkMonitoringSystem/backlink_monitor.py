import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# Replace these with your actual Moz API credentials
MOZ_ACCESS_ID = 'your_access_id'
MOZ_SECRET_KEY = 'your_secret_key'

def get_moz_metrics(url):
    try:
        # Construct the Moz API URL for metrics
        api_url = f"https://lsapi.seomoz.com/v2/url_metrics"
        headers = {
            'Authorization': f'Basic {MOZ_ACCESS_ID}:{MOZ_SECRET_KEY}',
            'Content-Type': 'application/json'
        }
        params = {
            "targets": [url]
        }
        
        response = requests.post(api_url, headers=headers, json=params)
        
        if response.status_code == 200:
            data = response.json()
            domain_authority = data['results'][0]['domain_authority']
            page_authority = data['results'][0]['page_authority']
            spam_score = data['results'][0]['spam_score']
            return domain_authority, page_authority, spam_score
        else:
            return None, None, None
            
    except Exception as e:
        print(f"Error fetching Moz metrics: {e}")
        return None, None, None

def check_backlink_status(backlink):
    try:
        response = requests.get(backlink)
        status_code = response.status_code
        
        # Check if the page contains a noindex tag
        soup = BeautifulSoup(response.content, 'html.parser')
        noindex_tag = soup.find('meta', attrs={'name': 'robots', 'content': 'noindex'})
        
        if noindex_tag:
            indexed_status = "Noindex"
        else:
            indexed_status = "Indexed"
        
        # Get Moz metrics
        domain_authority, page_authority, spam_score = get_moz_metrics(backlink)
        
        return (backlink, indexed_status, status_code, domain_authority, page_authority, spam_score)
    except requests.exceptions.RequestException as e:
        return (backlink, "Error", str(e), None, None, None)

def main():
    results = []
    
    # Read backlinks from file
    with open('urls.txt', 'r') as file:
        backlinks = file.readlines()
    
    # Analyze each backlink
    for backlink in backlinks:
        backlink = backlink.strip()  # Remove any leading/trailing whitespace/newline characters
        
        if backlink:  # Ensure that the backlink is not empty before processing
            result = check_backlink_status(backlink)
            results.append(result)
    
    # Convert results to DataFrame and save to CSV
    df_results = pd.DataFrame(results, columns=['Backlink', 'Status', 'Response Code', 
                                                'Domain Authority', 'Page Authority', 'Spam Score'])
    df_results.to_csv('output_results.csv', index=False)
    print("Backlink monitoring completed. Results saved to 'output_results.csv'.")

if __name__ == "__main__":
    main()
