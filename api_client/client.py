import requests
import logging

class APIClient:
    """Simple API client for practice."""

    def __init__(self, base_url):
        self.base_url = base_url
        logging.basicConfig(filename='logs.txt', level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s')

    def get_data(self, endpoint, verify=False):
        """Make a GET request to the API."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, verify=verify)
            logging.info(f"GET {url} - Status: {response.status_code} - Response: {response.text}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"GET {url} - Error: {e}")
            return {"error": str(e)}

    def post_data(self, endpoint, payload, verify=False):
        """Make a POST request to the API."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=payload, verify=verify)
            logging.info(f"POST {url} - Payload: {payload} - Status: {response.status_code} - Response: {response.text}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"POST {url} - Payload: {payload} - Error: {e}")
            return {"error": str(e)}
