import requests
from typing import List
from decouple import config
import urllib.parse


# Function to send SMS using Deywuro API (GET request)
def send_sms_get(destination: List[str], source: str, message: str) -> dict:
    base_url = "https://deywuro.com/api/sms/"

    # Loading credentials from the .env file
    username = config("DEYWURO_USERNAME")
    password = config("DEYWURO_PASSWORD")

    # Prepare the query parameters
    params = {
        "username": username,
        "password": password,
        "destination": ",".join(destination),  # Join numbers with commas
        "source": source,
        "message": message
    }

    # Encode the parameters for URL
    query_string = urllib.parse.urlencode(params)
    request_url = f"{base_url}?{query_string}"

    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()  # Return the response in JSON format
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"Other error occurred: {err}"}


# Example usage
if __name__ == "__main__":
    destination = ["233200000000", "2332000000", "233570000"]  # Destination contacts
    source = config('DEYWURO_SOURCE', cast=str)  # Approved Deywuro sender ID
    message = "Hi, this is a test message from {PLACEHOLDER}."  # Message to send

    result = send_sms_get(destination, source, message)
    print(result)
