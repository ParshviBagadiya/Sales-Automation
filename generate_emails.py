from jinja2 import Template
import pandas as pd

# Load your data (Excel from Task 1)
df = pd.read_excel("scraped_icp_companies_india.xlsx")

# Load the HTML email template
with open("email_template.html", "r") as f:
    template_content = f.read()

email_template = Template(template_content)

# Loop through data and create personalized emails
for index, row in df.iterrows():
    rendered_email = email_template.render(
        recipient_name="Team",  # You can update this if you have contact person
        company_name=row['Company Name'],
            industry=row['Industry']
    )

    # Optional: Save each rendered email to a file
    with open(f"emails/email_{index+1}.html", "w") as f:
        f.write(rendered_email)

    print(f"✅ Email {index+1} created for: {row['Company Name']}")
