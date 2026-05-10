def get_recommendation_prompt(content):
    return f"""
Analyze the following meeting minutes and provide exactly 3 actionable recommendations.
Data: {content}

Return ONLY a JSON array of objects.
Format:
[
  {{
    "action_type": "string (Task/Policy/Finance/Meeting)",
    "description": "string (The recommendation)",
    "priority": "string (High/Medium/Low)"
  }}
]
"""

def get_report_prompt(content, agenda):
    return f"""
Task: Create a formal Board Meeting Report.
Agenda Context: {agenda}
Raw Minutes: {content}

Return ONLY a JSON object with these exact keys:
{{
  "title": "Professional Report Title",
  "summary": "Executive summary (2 sentences)",
  "overview": "Detailed overview of discussions",
  "key_items": ["List of 3-5 main discussion points"],
  "recommendations": ["List of actionable steps"]
}}
"""
