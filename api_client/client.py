import requests

class APIClient:
    """Simple API client for practice."""

    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint, verify=False):
        """Make a GET request to the API."""
        response = requests.get(f"{self.base_url}/{endpoint}", verify=verify)
        if response.status_code == 200:
            return response.json()
        return {"error": response.status_code}

    def post_data(self, endpoint, payload, verify=False):
        """Make a POST request to the API."""
        response = requests.post(f"{self.base_url}/{endpoint}", json=payload, verify=verify)
        if response.status_code in [200, 201]:
            return response.json()
        return {"error": response.status_code}
