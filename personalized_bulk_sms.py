import csv
import requests
import json
from decouple import config


# Function to read CSV file and return data in a list format
def read_contacts_from_csv(file_path: str):
    contacts = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append({
                "name": row['name'],
                "phone": row['phone']
            })
    return contacts


# Function to send personalized SMS using Deywuro Personalized Bulk API
def send_personalized_sms_from_csv(file_path: str, sender_id: str):
    url = "https://bulk-api.deywuro.com/personalized-bulk/api"

    # Read contacts from CSV
    contacts = read_contacts_from_csv(file_path)

    # Prepare data for the API
    data = []
    for contact in contacts:
        personalized_message = f"Hello {contact['name']}, this is your personalized message!"
        data.append({
            "source": sender_id,
            "destination": contact['phone'],
            "message": personalized_message,
            "id": f"msg_{contact['name']}"
        })

    # Prepare the request payload
    payload = {
        "username": config('DEYWURO_USERNAME'),
        "password": config('DEYWURO_PASSWORD'),
        "data": data
    }

    # Set the request headers
    headers = {
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response.json()


# Example usage
file_path = "contacts.csv"  # Path to your CSV file
sender_id = config('DEYWURO_SOURCE')  # Pre-approved sender ID

response = send_personalized_sms_from_csv(file_path, sender_id)
print(response)
