import sys
from scrape import scrape_today
from download_video import download
from dotenv import load_dotenv  

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Loading environment variable")
        load_dotenv()
        
        print(f"Number of posts to scrape: {sys.argv[1]}")
        # Object containing "url" and "caption" of the scraped data
        scrape_result = scrape_today(int(sys.argv[1]))
        download(scrape_result)
    else:
        print("No arguments provided")
