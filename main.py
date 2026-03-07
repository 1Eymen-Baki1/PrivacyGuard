import requests
import json
import time

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Get your API key from https://aistudio.google.com/
API_KEY = "YOUR_API_KEY_HERE"

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

# Example Policy Text to Test
policy_text = """
(your_app_policy)
"""

# AI Prompt Configuration
prompt = f"""
You are an expert Data Privacy Lawyer. Your goal is to warn users by creating a flashy, emoji-rich, and eye-catching analysis.

Strictly follow these rules:
1. 🎯 RISK SCORE: Provide a score between 1 and 10. Next to the score, use one of these emojis based on risk: (🟢 Safe, 🟡 Caution, 🔴 Danger).
2. 📝 SHORT SUMMARY: List the 3 most critical points. Add a striking emoji (🚨, 👁️, 🕵️‍♂️, 📍, etc.) at the beginning of each point.
3. The output must be very clean, easy to read, and modern.

Text to Analyze: {policy_text}
"""

payload = {
    "contents": [{"parts": [{"text": prompt}]}]
}
headers = {'Content-Type': 'application/json'}

# Stylish CLI Boot Sequence
print(f"\n{Colors.CYAN}{Colors.BOLD}🛡️ PrivacyGuard AI Initializing...{Colors.RESET}")
time.sleep(1)
print(f"{Colors.YELLOW}🔍 Scanning privacy policy...{Colors.RESET}")
time.sleep(1.5)
print(f"{Colors.GREEN}⚙️ AI analysis complete! Displaying results...\n{Colors.RESET}")
print(f"{Colors.RED}{Colors.BOLD}{'-' * 50}{Colors.RESET}\n")

try:
    # Sending the Request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        data = response.json()
        ai_output = data['candidates'][0]['content']['parts'][0]['text']
        
        # Printing AI Analysis
        print(f"{Colors.BOLD}{ai_output}{Colors.RESET}")
    else:
        print(f"{Colors.RED}❌ Server Error: {response.status_code}{Colors.RESET}")
        print(response.text)
        
except Exception as error:
    print(f"{Colors.RED}❌ Connection Error: {error}{Colors.RESET}")

print(f"\n{Colors.RED}{Colors.BOLD}{'-' * 50}{Colors.RESET}\n")
