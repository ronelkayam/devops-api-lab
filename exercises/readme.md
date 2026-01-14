# API Exercise: JSONPlaceholder

## Public API Used
- API: JSONPlaceholder (https://jsonplaceholder.typicode.com)  
- Description: A free fake REST API for testing and prototyping.

---

## GET Request

**Endpoint:** `/posts`  
**Request URL:** `https://jsonplaceholder.typicode.com/posts`

**Description:**  
This GET request retrieves a list of posts from the API. Each post contains a `userId`, `id`, `title`, and `body`.

**Result:**  
- Status Code: `200 OK`  
- Example Response (first 3 posts):

```json
[
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit..."
    },
    {
        "userId": 1,
        "id": 2,
        "title": "qui est esse",
        "body": "est rerum tempore vitae..."
    },
    {
        "userId": 1,
        "id": 3,
        "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
        "body": "et iusto sed quo iure..."
    }
]


**Description:**  
This example demonstrates how to send a POST request to create a new post using `APIClient.post_data()`:

```python
payload = {
    "title": "Test Post",
    "body": "Post Result",
    "userId": 2
}

print("\nSending a POST request:")
response = client.post_data("posts", payload)
pretty_print(response)
```

**Result:**  
- Status Code: `201 Created`  
- Example Response:

```json
{
    "title": "Test Post",
    "body": "Post Result",
    "userId": 2,
    "id": 101
}
```