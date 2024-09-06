# Deywuro SMS API Integration

This project demonstrates how to integrate with the Deywuro Bulk SMS APIs to send SMS, check delivery reports, and monitor your credit balance.

## Features
- Send Bulk SMS
- Send Personalized Bulk SMS
- Single SMS (Send SMS v1 and v2)
- Query Delivery Reports (DLR)
- Check SMS Credit Balance
- Sentiment Analysis of SMS

## Requirements
- Python 3.x
- `requests` package
- `python-decouple` for environment variables

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/henryantwi/BulkSMSClient.git
    cd deywuro-api-integration
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory with your Deywuro credentials:
    ```bash
    USERNAME=your_deywuro_username
    PASSWORD=your_deywuro_password
    ```

## Usage

### Sending Bulk SMS
```python
from deywuro_sms import send_bulk_sms

# Example usage
destination = ["233200000", "2332500000"]
source = "Your Sender ID"
message = "Test Messages"
response = send_bulk_sms(destination, source, message)
print(response)
