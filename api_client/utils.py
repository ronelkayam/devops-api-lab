import json

def pretty_print(data):
    """Print JSON data in a readable way."""
    print(json.dumps(data, indent=4))
