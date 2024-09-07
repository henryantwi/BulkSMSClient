import requests
from decouple import config
import urllib.parse
import csv


# Function to send SMS using Deywuro API (GET request)
def send_sms_get(destination: str, message: str, source: str) -> dict:
    base_url = "https://deywuro.com/api/sms/"

    # Loading credentials from the .env file
    username = config("DEYWURO_USERNAME")
    password = config("DEYWURO_PASSWORD")

    # Prepare the query parameters
    params = {
        "username": username,
        "password": password,
        "destination": destination,
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


# Function to read CSV and send personalized messages
def send_personalized_messages(csv_file: str, source: str):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (role := row['role'].upper()) == 'MEMBER':
                name = row['name']
                phone = row['phone']
                message = f"Hi {name}, this is a personalized message from the UCM SRID team."
                result = send_sms_get(phone, message, source)
                print(f"Sent to {name} ({phone}): {result}")


# Example usage
if __name__ == "__main__":
    csv_file = 'data/contacts.csv'  # Path to your CSV file
    source = config('DEYWURO_SOURCE', cast=str)  # Approved Deywuro sender ID
    send_personalized_messages(csv_file, source)
