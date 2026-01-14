from api_client.client import APIClient
from api_client.utils import pretty_print

def main():
    client = APIClient("https://jsonplaceholder.typicode.com")

    # GET request example
    print("Fetching first 3 posts:")
    posts = client.get_data("posts")[:3]
    pretty_print(posts)

    # POST request example
    payload = {
        "title": "Test Post",
        "body": "Post Result",
        "userId": 2
    }
    print("\nSending a POST request:")
    response = client.post_data("posts", payload)
    pretty_print(response)

if __name__ == "__main__":
    main()
