import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='seo_analysis.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def seo_analysis(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code != 200:
            logging.error(f"Failed to retrieve {url}: Status code {response.status_code}")
            return {"URL": url, "Error": "Failed to retrieve"}
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title tag
        title = soup.title.string if soup.title else "No title found"
        
        # Extract meta description
        meta_description = soup.find('meta', attrs={'name': 'description'})
        meta_description_content = meta_description['content'] if meta_description else "No meta description found"
        
        # Extract meta keywords
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        meta_keywords_content = meta_keywords['content'] if meta_keywords else "No meta keywords found"

        # Robots tag
        robots_tag = soup.find('meta', attrs={'name': 'robots'})
        robots_content = robots_tag['content'] if robots_tag else "No robots tag found"

        # Word count
        word_count = len(soup.get_text().split())

        # H1 tags
        h1_tags = soup.find_all('h1')
        h1_count = len(h1_tags)

        # Total links
        all_links = soup.find_all('a')
        total_links = len(all_links)

        # Internal and external links
        internal_links = [link for link in all_links if url in link.get('href', '')]
        external_links = [link for link in all_links if url not in link.get('href', '')]

        # Count images and check for alt attributes
        images = soup.find_all('img')
        total_images = len(images)
        images_without_alt = [img for img in images if not img.get('alt')]
        images_without_title = [img for img in images if not img.get('title')]

        # Schema data (example: checking for JSON-LD)
        schema_data = soup.find_all('script', type='application/ld+json')
        schema_count = len(schema_data)

        # Hreflang tags
        hreflang_tags = soup.find_all('link', attrs={'rel': 'alternate', 'hreflang': True})
        
        # Open Graph and Twitter Card data
        open_graph_tags = {tag['property']: tag['content'] for tag in soup.find_all('meta') if tag.get('property')}
        twitter_card_tags = {tag['name']: tag['content'] for tag in soup.find_all('meta') if tag.get('name')}

        # Log the results
        logging.info(f"URL: {url}")
        logging.info(f"Title: {title}")
        logging.info(f"Meta Description: {meta_description_content}")
        logging.info(f"Meta Keywords: {meta_keywords_content}")
        logging.info(f"Robots Tag: {robots_content}")
        logging.info(f"Word Count: {word_count}")
        logging.info(f"H1 Count: {h1_count}")
        logging.info(f"Total Links: {total_links}")
        logging.info(f"Internal Links: {len(internal_links)}")
        logging.info(f"External Links: {len(external_links)}")
        logging.info(f"Total Images: {total_images}")
        logging.info(f"Images Without Alt: {len(images_without_alt)}")
        logging.info(f"Images Without Title: {len(images_without_title)}")
        logging.info(f"Schema Count: {schema_count}")
        
        return {
            "URL": url,
            "Title": title,
            "Meta Description": meta_description_content,
            "Meta Keywords": meta_keywords_content,
            "Robots Tag": robots_content,
            "Word Count": word_count,
            "H1 Count": h1_count,
            "Total Links": total_links,
            "Internal Links": len(internal_links),
            "External Links": len(external_links),
            "Total Images": total_images,
            "Images Without Alt": len(images_without_alt),
            "Images Without Title": len(images_without_title),
            "Schema Count": schema_count,
            "Hreflang Tags": len(hreflang_tags),
            "Open Graph Tags": len(open_graph_tags),
            "Twitter Card Tags": len(twitter_card_tags),
            "Error": None
        }
    
    except Exception as e:
        logging.error(f"Error processing {url}: {e}")
        return {"URL": url, "Error": str(e)}

def main():
    results = []
    
    # Read URLs from file
    with open('urls.txt', 'r') as file:
        urls = file.readlines()
    
    # Analyze each URL
    for url in urls:
        url = url.strip()  # Remove any leading/trailing whitespace/newline characters
        result = seo_analysis(url)
        
        results.append(result)
    
    # Convert results to DataFrame and save to CSV
    df_results = pd.DataFrame(results)
    df_results.to_csv('output_results.csv', index=False)
    print("SEO analysis completed. Results saved to 'output_results.csv'.")

if __name__ == "__main__":
    main()