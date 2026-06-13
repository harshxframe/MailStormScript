from mailjet_rest import Client
import os
from dotenv import load_dotenv
import sys
load_dotenv()

 
# 1. EDIT THESE WITH YOUR MAILJET CREDENTIALS
API_KEY =  os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
KOREXBASE_LINK = 'https://www.korexbase.com/'  # Add your exact signup link here


# Initialize Mailjet Client
mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

# 2. ARRAY OF 50 EXTRACTED LEADS FROM YOUR EXCEL FILES
leads_array = [
    # {'Business Name': 'Saber Data', 'First Email': 'info@saberdata.com'},
]

# 3. BUILD THE BULK MESSAGE PAYLOAD
messages = []
for lead in leads_array:
    # Clean up the business name in case it's too long
    clean_business_name = lead['Business Name'].split('|')[0].split('-')[0].strip()
    
    html_body = f"""
    <p>Hey {clean_business_name} team,</p>
    <p>I saw you clicked through to check out Korexbase Leads earlier but maybe didn't get a chance to run a full scrape.</p>
    <p>As a solo founder, I want to make sure you actually get to see the data quality firsthand. If you reply directly to this email with a <strong>city</strong> and a <strong>business niche</strong> you are targeting right now, I will personally run the scraper and email you the CSV directly. No need to even create an account.</p>
    <p>Let me know what data you need!</p>
    <p>Cheers,<br>Harsh<br>Founder, Korexbase</p>
    """

    message = {
        "From": {
            "Email": "no-reply@korexbase.com",
            "Name": "Harsh at Korexbase"
        },
        "To": [
            {
                "Email": lead['First Email'],
                "Name": clean_business_name
            }
        ],
        "ReplyTo": {
            "Email": "harsh@korexbase.com",
            "Name": "Harsh"
        },
        "Subject": "Quick question regarding Korexbase data",
        "HTMLPart": html_body
    }
    messages.append(message)

# 4. EXECUTE BATCH SEND (Mailjet allows up to 50 messages per API call)
data = {
  'Messages': messages
}

print(f"Sending batch of {len(messages)} emails via Mailjet...")
result = mailjet.send.create(data=data)

# Print the results
if result.status_code == 200:
    print("Success! All emails dispatched.")
else:
    print(f"Failed with status code: {result.status_code}")
    print(result.json())