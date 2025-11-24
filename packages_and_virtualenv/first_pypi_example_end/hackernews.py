# import the requests package into your code.
import requests

def get_top_ten_headlines():
    headlined_ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()[:10]
    return headlined_ids

def get_headline_by_id(headline_id):
    headline = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{headline_id}.json").json()
    return headline

def main():
    top_ten_ids = get_top_ten_headlines()
    for index, id in enumerate(top_ten_ids):
        headline = get_headline_by_id(id)
        print(f"Headline {index + 1}.")
        print(f"Title: {headline['title']}")
        print(f"URL: {headline.get('url', 'No URL available')}")
        print("-" * 40)

if __name__ == "__main__":
    main()