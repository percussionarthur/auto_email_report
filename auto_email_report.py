#!/usr/bin/python3

import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

# Email configuration
smtp_server = "smtp.gmail.com"  # Change this if using a different service
smtp_port = 587
sender_email = "sender@example.com" # Change before executing
sender_password = "xxxx xxxx xxxx xxxx" # Requires the use of Google's app password feature
receiver_email = "receiver@example.com" # Change before executing

def send_email_report():
    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Daily Report - {}".format(datetime.now().strftime("%Y-%m-%d"))

    # Add the email body
    sent_date = f"Subject: {msg['Subject']}"
    body = """

Dear Team,

Please find below the summary of today\’s report:

---

**Summary:**

- **Key Highlights:**
- [Highlight or update related to current tasks]
- [Additional information on team progress]

- **Performance Metrics:**
- [Metric 1]: [Value or percentage]
- [Metric 2]: [Value or percentage]

- **Notes:**
- Reminder: The next meeting is scheduled for [Meeting Date].
- No additional actions required at this time.

---

If you have any questions or need further details, please do not hesitate to reach out.

Best regards,

Arthur Lin
"""

    msg.attach(MIMEText((sent_date + body), 'plain'))

    # Send the email via the SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print(f"Email sent successfully to {receiver_email}!")

    except Exception as e:
        print(f"Error sending email: {str(e)}")

    finally:
        server.quit()

# Schedule the email to send daily at 8 AM
def schedule_daily_email():
    schedule.every().day.at("20:25").do(send_email_report)
    
    print("Scheduler is running. Waiting for the next email send time...")

    # Keep the script running to trigger the email at the scheduled time
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

# Only executed when script is run directly and not imported
if __name__ == "__main__":
    schedule_daily_email()
