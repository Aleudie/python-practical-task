"""
Task 2. This script: 
- Creates a survey 
- Creates a collector for the survey
- Creates a message for the collector
- Adds recipients for the message
    - Each recipient its taken from a text file with a list of email addresses
"""

#!/usr/bin/env python

import os
import json
import http.client
from argparse import ArgumentParser

parser = ArgumentParser(description='Creates a survey using SurveyMonkey API')
parser.add_argument('emails_filename',
                    default='emails_example.txt',
                    help='Filename of the txt file with emails')
parser.add_argument('survey_filename',
                    default='survey_example.json',
                    help='Filename of the json survey file')
args = parser.parse_args()

access_token = os.getenv("ACCESS_TOKEN")
if not access_token:
    raise EnvironmentError("ACCESS_TOKEN environment variable not set")

conn = http.client.HTTPSConnection("api.surveymonkey.com")
headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': "Bearer " + access_token
}

# Load emails and validate at least 2
with open(args.emails_filename, "r", encoding="utf-8") as f:
    payload = f.read()
emails = [line.strip() for line in payload.splitlines() if line.strip()]
if len(emails) < 2:
    raise ValueError("emails file must contain at least 2 email addresses")

# Load survey and validate at least 3 questions
with open(args.survey_filename, "r", encoding="utf-8") as f:
    payload = f.read()
survey_data = json.loads(payload)
questions = survey_data.get("pages", [])[0].get("questions", []) if survey_data.get("pages") else []
if len(questions) < 3:
    raise ValueError("survey file must contain at least 3 questions")

# Create a survey
conn.request("POST", "/v3/surveys", payload, headers)
res = conn.getresponse()
data = res.read()

# Print preview link of the survey
response_json = json.loads(data.decode("utf-8"))
print(response_json.get("preview"))

# Creates a collector for the survey
conn.request("POST", "/v3/surveys/" + response_json.get("id") + "/collectors", '{"type": "email"}', headers)
res = conn.getresponse()
data = res.read()
response_json = json.loads(data.decode("utf-8"))
print("Status:", res.status)
print(response_json)

# Creates a message for the collector
with open("message_example.json", "r") as f:
    payload = f.read()

conn.request("POST", "/v3/collectors/" + response_json.get("id") + "/messages", payload, headers)
res = conn.getresponse()
data = res.read()
response_json = json.loads(data.decode("utf-8"))
print("Status:", res.status)
print(response_json)
