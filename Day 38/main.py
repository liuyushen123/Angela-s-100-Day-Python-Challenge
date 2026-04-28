import datetime as dt
import json
import os

import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()
today = dt.datetime.now()
today = today.strftime("%b %d %a %Y")
url = "https://api.sheety.co/9ec77ccb1f24490364afb4e3c6666ba0/trackWorkout/trackWorkout"
user_input = input("Tell me which exercises you did: ")
output_schema = """
{
  "user_profile": {
    "weight_kg": 0,
    "age": 0,
    "gender": ""
  },
  "activities": [
    {
      "original_phrase": "string",
      "mapped_activity": "string",
      "duration_minutes": 0,
      "met_value": 0.0,
      "calories_burned": 0.0
    }
  ],
  "total_calories_burned": 0.0
}
"""
PROMPT = f"""
    INSTRUCTIONS:
    1. Extract all exercises from the input.
    2. For each exercise, determine:
    - name (lowercase, single word if possible)
    - duration in minutes (integer)
    - MET value (use standard estimates)
    3. Calculate calories using:
    calories = MET × weight_kg × (duration_minutes / 60)
    4. Round calories to the nearest integer.
    5. If multiple activities exist, include all of them.
    6. Compute total_calories as the sum.

    STRICT OUTPUT RULES:
    - Return ONLY valid JSON
    - Do NOT include explanations, text, or markdown
    - Do NOT wrap in ```json
    - Ensure all keys and strings use double quotes
    - Ensure JSON is parsable by Python json.loads()
    This is an output schema: {output_schema}

    - Weight: 91kg
    - Age: 22
    - Gender: male
    - Input: {user_input}

"""


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
response = client.models.generate_content(model="gemini-2.5-flash", contents=PROMPT)
response = response.text.strip()
cleaned = response.replace("```json", "").replace("```", "").strip()
data = json.loads(cleaned)

for act in data["activities"]:
    sheet_data = {
        "trackworkout": {
            "date": today,
            "exercise": act["mapped_activity"],
            "duration": act["duration_minutes"],
            "calories": act["calories_burned"],
        }
    }

    requests.post(url=url, json=sheet_data)
