#Generic script based off original main, if you want to run something use this as base

"""
example_email_alert.py

Example Python script to send HTML+plain-text emails using SMTP.
Template only - fill in your own email credentials and content.
"""

import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# === Configure these before use ===
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
EMAIL_RECEIVER = "recipient@example.com"
EMAIL_CC = "optional_cc@example.com"

SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

def build_email(subject: str, plain_text: str, html_body: str) -> MIMEMultipart:
    message = MIMEMultipart("alternative")
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER
    message["Cc"] = EMAIL_CC
    message["Subject"] = subject

    part1 = MIMEText(plain_text, "plain")
    part2 = MIMEText(html_body, "html")

    message.attach(part1)
    message.attach(part2)
    return message

def send_email(message: MIMEMultipart):
    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(
            EMAIL_SENDER,
            [EMAIL_RECEIVER] + [EMAIL_CC],
            message.as_string()
        )
    print("Email sent successfully.")

def main():
    # Example dynamic content
    branch_name = "Example Branch"
    branch_ip = "192.0.2.1"
    address = "123 Example Street"
    service_code = "ABC123"

    subject = f"Alert: Issue detected at {branch_name}"
    plain_text = f"""\
Hello,

An issue has been detected at {branch_name}.

IP: {branch_ip}
Address: {address}
Service Code: {service_code}

Please investigate.

Regards,
Automated Alert System
"""

    html_body = f"""\
<html>
  <body>
    <h2>Alert: Issue detected at {branch_name}</h2>
    <p><strong>IP:</strong> {branch_ip}</p>
    <p><strong>Address:</strong> {address}</p>
    <p><strong>Service Code:</strong> {service_code}</p>
    <p>Please investigate.</p>
  </body>
</html>
"""

    message = build_email(subject, plain_text, html_body)
    send_email(message)

if __name__ == "__main__":
    main()
