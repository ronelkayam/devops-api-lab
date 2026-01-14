from api_client.client import APIClient
from api_client.utils import pretty_print

def main():
    client = APIClient("https://jsonplaceholder.typicode.com/posts")

    # GET request example
    print("Fetching first 3 posts:")
    posts = client.get_data("")[:3]
    pretty_print(posts)

    # POST request example
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    print("\nSending a POST request:")
    response = client.post_data("", payload)
    pretty_print(response)

def test_asher():
    print("this is test from asher")

test_asher()
if __name__ == "__main__":
    main()
