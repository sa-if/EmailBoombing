import smtplib
import ssl
import time

def send_email(receiver_emails, message):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email_address"
    app_password = "your_app_password"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Log in to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)
        server.login(sender_email, app_password)
        for receiver_email in receiver_emails:
            server.sendmail(sender_email, receiver_email, message)

# Example usage
receiver_emails = ["example@example.com", "example@example.com"] # you can add multiple receiver if one then use only one email
message = "This is a test email sent using Python."

while True:
    send_email(receiver_emails, message)
    time.sleep(1)  # wait for 60 seconds before sending the next email
