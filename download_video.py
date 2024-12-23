from apify_client import ApifyClient
from datetime import datetime
import os
import json


def download(input):
    APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
    client = ApifyClient(APIFY_API_TOKEN)

    # Prepare the Actor input
    run_input = {
        "startUrls": [item["url"] for item in input],
        "proxy": { "useApifyProxy": True },
    }

    # Run the Actor and wait for it to finish
    run = client.actor("OWBUCWZK5MEeO5XiC").call(run_input=run_input)
    result = client.dataset(run["defaultDatasetId"])
    result_list = result.list_items().items
    today_date = datetime.today().strftime('%Y-%m-%d')
    target_directory = f"result/{today_date}"
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    file_path = f"{target_directory}/download_data.json"
    with open(file_path, "w") as f:
        json.dump(result_list, f)
    print(f"Download results saved to {file_path}")

    url_caption_mapping = {item["url"]: item["caption"] for item in input}
    result_mapped = [
        {
            "IGUrl": item["sourceUrl"],
            "caption": url_caption_mapping[item["sourceUrl"]],
            "downloadUrl": item["downloadUrl"],
        }
        for item in result_list
    ]

    file_path_final = f"{target_directory}/download_data_mapped.json"
    with open(file_path_final, "w") as f:
        json.dump(result_mapped, f) 
    print(f"Download results mapped saved to {file_path_final}")
