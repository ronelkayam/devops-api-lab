# Exercises for DevOps Students

## Git Tasks

1. Pull the latest version of the repo:

git pull origin main
Create a branch for your group:


git checkout -b group1
Work on your exercise files (demo.py or new scripts).

Commit your changes:



git add .
git commit -m "Added GET request exercise"
Push your branch to GitHub:


git push origin group1
Create a Pull Request to merge into main.

Python API Tasks
GET request:

Use APIClient.get_data() to fetch posts from:
https://jsonplaceholder.typicode.com/posts

Print the first 3 posts using utils.pretty_print.

POST request:

Use APIClient.post_data() to send data to:
https://jsonplaceholder.typicode.com/posts

Example payload:

json
Copy code
{
    "title": "foo",
    "body": "bar",
    "userId": 1
}
Group Exercise:

Each group picks a public API (like httpbin) and implements:

GET requests

POST requests

Document results in a new Markdown file inside exercises/.

Bonus:

Add error handling for failed requests.

Log responses into a file logs.txt.