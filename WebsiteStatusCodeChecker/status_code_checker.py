import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import socket

def get_metrics(url):
    metrics = {}
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        
        # Calculate response time
        metrics['Response Time (ms)'] = round((time.time() - start_time) * 1000, 2)  # in milliseconds
        
        # Get HTTP status code
        metrics['Status Code'] = response.status_code
        
        # Check for redirection
        if response.history:
            metrics['Redirection'] = ' -> '.join([str(resp.status_code) for resp in response.history] + [str(response.status_code)])
            metrics['Final URL'] = response.url
        else:
            metrics['Redirection'] = 'None'
            metrics['Final URL'] = url
        
        # Get content type and length
        metrics['Content Type'] = response.headers.get('Content-Type', 'N/A')
        metrics['Content Length (bytes)'] = response.headers.get('Content-Length', 'N/A')
        
        # Get server type
        metrics['Server Type'] = response.headers.get('Server', 'N/A')
        
        # Get IP address using socket
        ip_address = socket.gethostbyname(requests.utils.urlparse(url).hostname)
        metrics['IP Address'] = ip_address
        
        # Check SSL/TLS status (if applicable)
        if url.startswith("https://"):
            metrics['SSL/TLS Status'] = "Valid"
        else:
            metrics['SSL/TLS Status'] = "N/A"
        
    except requests.exceptions.RequestException as e:
        metrics['Status Code'] = f"Error: {e}"
    
    return metrics

def crawl_website(base_url):
    try:
        response = requests.get(base_url)
        if response.status_code != 200:
            print(f"Failed to retrieve {base_url}: {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        links = set()
        
        # Extract all anchor tags with href attributes
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/'):
                href = base_url + href
            elif not href.startswith('http'):
                continue
            
            links.add(href)

        return list(links)
    except Exception as e:
        print(f"Error crawling {base_url}: {e}")
        return []

def main():
    results = []
    
    with open('urls.txt', 'r') as file:
        base_urls = file.readlines()
    
    for base_url in base_urls:
        base_url = base_url.strip()
        
        if base_url:  
            print(f"Crawling: {base_url}")
            found_links = crawl_website(base_url)
            
            for link in found_links:
                metrics = get_metrics(link)
                results.append({**{'URL': link}, **metrics})
    
    df_results = pd.DataFrame(results)
    df_results.to_csv('output_results.csv', index=False)
    print("Status code checking completed. Results saved to 'output_results.csv'.")

if __name__ == "__main__":
    main()