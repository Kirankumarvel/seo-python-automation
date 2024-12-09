import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import json

# Configure logging
logging.basicConfig(
    filename='seo_analysis.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_page_speed_metrics(url):
    # Placeholder function for getting page speed metrics
    # In a real implementation, you would use an API like Google PageSpeed Insights
    return {
        "LCP": "N/A",  # Largest Contentful Paint
        "INP": "N/A",  # Interaction to Next Paint
        "CLS": "N/A"   # Cumulative Layout Shift
    }

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

        # Canonical tag
        canonical_tag = soup.find('link', attrs={'rel': 'canonical'})
        canonical_content = canonical_tag['href'] if canonical_tag else "No canonical tag found"

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
        
        # Types of schema found (if any)
        schema_types = [json.loads(schema.string).get('@type') for schema in schema_data] if schema_data else []
        
        # Hreflang tags
        hreflang_tags = soup.find_all('link', attrs={'rel': 'alternate', 'hreflang': True})
        
        # Open Graph and Twitter Card data
        open_graph_tags = {tag['property']: tag['content'] for tag in soup.find_all('meta') if tag.get('property')}
        twitter_card_tags = {tag['name']: tag['content'] for tag in soup.find_all('meta') if tag.get('name')}
        
        # Get page speed metrics (placeholder)
        page_speed_metrics = get_page_speed_metrics(url)

        # Log the results before returning them
        logging.info(f"URL: {url}")
        logging.info(f"Title: {title}")
        logging.info(f"Meta Description: {meta_description_content}")
        logging.info(f"Meta Keywords: {meta_keywords_content}")
        logging.info(f"Robots Tag: {robots_content}")
        logging.info(f"Canonical Tag: {canonical_content}")
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
            "Canonical": canonical_content,
            "Word Count": word_count,
            "H1 Count": h1_count,
            "Total Links": total_links,
            "Internal Links": len(internal_links),
            "External Links": len(external_links),
            "Total Images": total_images,
            "Images Without Alt": len(images_without_alt),
            "Images Without Title": len(images_without_title),
            "Schema Count": schema_count,
            "Schema Types": schema_types,
            "Hreflang Tags": len(hreflang_tags),
            "Open Graph Tags": len(open_graph_tags),
            "Twitter Card Tags": len(twitter_card_tags),
            **page_speed_metrics,  # Include page speed metrics in the result dictionary
            "Error": None
        }
    
    except Exception as e:
        logging.error(f"Error processing {url}: {e}")
        return {"URL": url, "Error": str(e)}

def main():
    results = []
    
    try:
       # Read URLs from file
       with open('urls.txt', 'r') as file:
           urls = file.readlines()
       
       # Analyze each URL
       for url in urls:
           url = url.strip()  # Remove any leading/trailing whitespace/newline characters

           if url:  # Ensure that the URL is not empty before processing
               result = seo_analysis(url)
               results.append(result)
           else:
               logging.warning("Empty URL encountered. Skipping.")

       # Convert results to DataFrame and save to CSV
       df_results = pd.DataFrame(results)
       df_results.to_csv('output_results.csv', index=False)
       print("SEO analysis completed. Results saved to 'output_results.csv'.")

    except FileNotFoundError:
       print("The file 'urls.txt' does not exist. Please ensure it is present.")
    except Exception as e:
       print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
