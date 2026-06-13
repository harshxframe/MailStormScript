# Mailjet Bulk Emailer

A Python-based automation tool to send personalized cold outreach emails via Mailjet.

## Features
- **Personalization:** Dynamically inserts business names and emails into templates.
- **Data Cleaning:** Automatically cleans business names by stripping common delimiters like `|` or `-`.
- **Environment Safety:** Uses `.env` files to keep API credentials secure.

## Prerequisites
- Python 3.x
- Mailjet Account and API Credentials

## Setup
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd MAILSTORM
   ```

2. **Install Dependencies:**
   ```bash
   pip install mailjet_rest python-dotenv
   ```

3. **Environment Variables:**
   Create a `.env` file in the root directory and add your credentials:
   ```env
   API_KEY=your_mailjet_api_key
   API_SECRET=your_mailjet_api_secret
   ```

4. **Prepare Leads:**
   Update the `leads_array` in `main.py` with your extracted lead data.

## Usage
Run the script:
```bash
python main.py
```
