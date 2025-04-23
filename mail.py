import smtplib
import pandas as pd
import time
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template
import os

EMAIL = 'jineshbakhai59@gmail.com'
PASSWORD = 'erbo duwy yirf urmv'

# Load lead data
df = pd.read_excel("scraped_icp_companies_india.xlsx")

# Load email template
with open("email_template.html", "r") as f:
    html_template = Template(f.read())

# Email sender function
def send_email(to_email, subject, body_html, body_plain):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    # Attach plain text and HTML parts
    part1 = MIMEText(body_plain, "plain")
    part2 = MIMEText(body_html, "html")
    msg.attach(part1)
    msg.attach(part2)

    # Connect and send
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to_email, msg.as_string())

# Loop through leads and send emails
for i, row in df.iterrows():
    recipient_email = row.get("Email", "parshvibagadiya@gmail.com")  # Replace with real field
    company_name = row.get("Company Name", "a company")
    industry = row.get("Industry", "your industry")
    # Example lead data
    lead_id = "lead_002"

    email_body_html = html_template.render(
        recipient_name="Team",  # Or use row.get("Contact Person", "Team")
        company_name=company_name,
        industry=industry,
        lead_id = lead_id
    )

    email_body_plain = (
        f"Hi Team,\n\n"
        f"I wanted to connect with {company_name} and share how our solutions "
        f"are helping companies in the {industry} industry streamline operations "
        f"and grow faster.\n\n"
        f"Let me know if you're open to a quick chat!\n\nBest,\nYour Name"
    )

    subject = f"Helping {company_name} grow with smart automation"



    try:
        send_email(recipient_email, subject, email_body_html, email_body_plain)
        print(f"✅ Email sent to: {recipient_email}")

        with open("email_log.txt", "a") as log:
            log.write(f"{time.ctime()} - Sent to: {recipient_email}\n")

    except Exception as e:
        print(f"❌ Failed to send to {recipient_email}: {e}")
        time.sleep(30)  # backoff on failure
        continue
    
    # Delay to avoid spam filters
    time.sleep(random.randint(5, 10))
