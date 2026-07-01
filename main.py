from mailjet_rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

# Add your leads here
leads_array = [
    {"Business Name": "Branding Los Angeles", "First Email": "info@brandinglosangeles.com"},
    {"Business Name": "HYPE Hyperion Digital Marketing Agency", "First Email": "contact@hypehyperion.com"},
    {"Business Name": "Eclipse Marketing - Los Angeles SEO Agency", "First Email": "contact@eclipsemarketing.io"},
    {"Business Name": "PurpleZ Marketing Agency", "First Email": "info@purplez.com"},
    {"Business Name": "Melleka Marketing - A Top Rated Digital Marketing Agency", "First Email": "contact@melleka.com"},
    {"Business Name": "SeedX Inc.", "First Email": "hello@seedx.us"},
    {"Business Name": "LikeSocialBiz", "First Email": "info@likesocialbiz.com"},
    {"Business Name": "Meshroad Marketing", "First Email": "sunil@meshroad.com"},
    {"Business Name": "Formula Internet", "First Email": "mark@formulainternet.com"},
    {"Business Name": "SPICY TRIBE", "First Email": "hi@spicytribe.com"},
    {"Business Name": "Media Distribution Services (MDS)", "First Email": "johnd@jdgsolution.com"},
    {"Business Name": "Modern Practice", "First Email": "contact@modernpractice.com"},
    {"Business Name": "Lightdrop", "First Email": "hello@lightdrop.com"},
    {"Business Name": "Tower 25 Digital Marketing Agency", "First Email": "info@tower25.com"},
    {"Business Name": "LAD Solutions", "First Email": "contactus@ladsolutions.com"},
    {"Business Name": "BlackGrid Digital", "First Email": "hello@blackgridseo.com"},
    {"Business Name": "Just Digital Inc.", "First Email": "info@justdigitalinc.com"},
    {"Business Name": "NuORDER", "First Email": "heroes@nuorder.com"},
    {"Business Name": "LaV1 - Los Angeles Digital Marketing & SEO", "First Email": "info@lav1.com"},
    {"Business Name": "Canesta Digital Marketing", "First Email": "info@canesta.com"},
    {"Business Name": "L.A. Social Karma", "First Email": "hello@lasocialkarma.com"},
    {"Business Name": "Brandastic", "First Email": "hello@brandastic.com"},
    {"Business Name": "Digital Traffik Agency", "First Email": "info@digitaltraffikagency.com"},
    {"Business Name": "Coalition Technologies", "First Email": "sales@coalitiontechnologies.com"},
    {"Business Name": "LawRank", "First Email": "hello@lawrank.com"},
    {"Business Name": "HawkSEM", "First Email": "info@hawksem.com"},
    {"Business Name": "Flying V Group", "First Email": "hello@flyingvgroup.com"},
    {"Business Name": "Single Grain", "First Email": "hello@singlegrain.com"},
    {"Business Name": "Infinity Media", "First Email": "hello@infinitymedia.io"},
    {"Business Name": "SEO Noble", "First Email": "info@seonoble.com"},
    {"Business Name": "RankPay", "First Email": "support@rankpay.com"},
    {"Business Name": "Storm Brain", "First Email": "hello@stormbrain.com"},
    {"Business Name": "Social House Inc.", "First Email": "hello@socialhouseinc.com"},
    {"Business Name": "Kobe Digital", "First Email": "hello@kobedigital.com"},
    {"Business Name": "Directive", "First Email": "sales@directiveconsulting.com"},
    {"Business Name": "SunCity Advising", "First Email": "info@suncityadvising.com"},
    {"Business Name": "VisualFizz", "First Email": "hello@visualfizz.com"},
    {"Business Name": "Top Growth Marketing", "First Email": "info@topgrowthmarketing.com"},
]

messages = []

for lead in leads_array:
    clean_business_name = lead["Business Name"].split("|")[0].split("-")[0].strip()

    html_body = f"""
    <html>
    <body style="font-family: Arial, Helvetica, sans-serif; color:#333; line-height:1.6;">

    <p>Hi {clean_business_name} Team,</p>

    <p>I'm Harsh, founder of Korexbase.</p>

    <p>I recently built a lead generation platform designed for agencies that want to own their own lead generation software instead of relying on expensive monthly tools.</p>

    <p>With Korexbase you can:</p>

    <ul>
        <li>Search businesses by niche & location</li>
        <li>Get business emails, phone numbers and websites</li>
        <li>Export clean CSV files instantly</li>
        <li>Run it under your own brand (white-label)</li>
        <li>Own the platform with a one-time purchase</li>
    </ul>

    <p>If your agency has ever considered launching its own lead generation platform, this could save months of development time.</p>

    <p>You can see the live demo here:</p>

    <p>
        <a href="https://www.korexbase.com/">
            https://www.korexbase.com/
        </a>
    </p>

    <p>If it looks interesting, just reply to this email and I'll personally give you a 10-minute demo and answer any questions.</p>

    <p>
    Thanks,<br><br>

    <strong>Harsh</strong><br>
    Founder, Korexbase<br>
    https://www.korexbase.com/
    </p>

    </body>
    </html>
    """

    messages.append({
        "From": {
            "Email": "no-reply@korexbase.com",
            "Name": "Harsh @ Korexbase"
        },
        "To": [
            {
                "Email": lead["First Email"],
                "Name": clean_business_name
            }
        ],
        "ReplyTo": {
            "Email": "harsh@korexbase.com",
            "Name": "Harsh"
        },
        "Subject": "White-label lead generation platform for agencies",
        "HTMLPart": html_body
    })

data = {
    "Messages": messages
}

print(f"Sending {len(messages)} emails...")

result = mailjet.send.create(data=data)

if result.status_code == 200:
    print("✅ Emails sent successfully!")
else:
    print(f"❌ Failed ({result.status_code})")
    print(result.json())