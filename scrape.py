from apify_client import ApifyClient
from datetime import datetime
import os
import json

def scrape_today(num_posts_limit=10):
    APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
    client = ApifyClient(APIFY_API_TOKEN)

    run_input = {
        "hashtags": ["yncdraco"],
        "resultsType": "posts",
        "resultsLimit": num_posts_limit,
    }

    print("Running actor")
    run = client.actor("reGe1ST3OBgYZSsZJ").call(run_input=run_input)
    result = client.dataset(run["defaultDatasetId"])
    result_list = result.list_items().items
    today_date = datetime.today().strftime('%Y-%m-%d')
    
    target_directory = f"result/{today_date}"
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    file_path = f"{target_directory}/scrape_data.json"
    with open(file_path, "w") as f:
        json.dump(result_list, f)
    print(f"Scrape results saved to {file_path}")

    result_cleaned = [
        {"url": item.get("url", None), "caption": item.get("caption", None)} 
        for item in result_list
        ]
    file_path_cleaned = f"{target_directory}/scrape_data_cleaned.json"
    with open(file_path_cleaned, "w") as f:
        json.dump(result_cleaned, f)
    print(f"Scrape results cleaned saved to {file_path_cleaned}")
    return result_cleaned