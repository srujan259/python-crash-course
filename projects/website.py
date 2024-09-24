import requests

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 404:
            send_email(url)
        else:
            print(f"URL responded with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking URL: {e}")

def send_email(url):
    sender_email = "your_email@example.com"
    receiver_email = "recipient@example.com"

    subject = "URL Check Alert: 404 Not Found"
    body = f"The following URL returned a 404 Not Found status:\n\n{url}"

    # Mimic sending the email by printing the details to the console
    print("Mimicking email send...")
    print(f"From: {sender_email}")
    print(f"To: {receiver_email}")
    print(f"Subject: {subject}")
    print("Body:")
    print(body)
    print("Email sent successfully (mimicked).")

if __name__ == "__main__":
    url_to_check = "https://www.google.com"
    check_url(url_to_check)