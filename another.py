from api_client.client import APIClient
from api_client.utils import pretty_print
import json

def main():
    client = APIClient("https://jsonplaceholder.typicode.com")

    # GET request example
    print("Fetching first 3 posts:")
    posts = client.get_data("posts")[:3]
    pretty_print(posts)

    # write first 3 objects to file
    with open("todos.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2)

    print("Saved first 3 posts to todos.json")

    # POST request example
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    print("\nSending a POST request:")
    response = client.post_data("posts", payload)
    pretty_print(response)

if __name__ == "__main__":
    main()
