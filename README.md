# auto_email_report

This Python script automates sending daily email reports using Gmail's SMTP server. It schedules the task with the schedule library and allows for optional attachments.

Requirements:
- Python 3

Required libraries:
- smtplib (comes pre-installed with Python)
- email.mime (comes pre-installed with Python)
- schedule (install with pip install schedule)

Functions:

1. Email Setup
Configures email parameters, including sender’s email, password, and recipient’s email.
2. Email Content
Constructs the email with a subject line and body text.
3. Scheduling
Uses the schedule library to run the email-sending function at a specified time each day.
4. Sending Email
Connects to Gmail’s SMTP server, logs in with the sender’s credentials, and sends the email to the recipient.
