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
  "key_items": ["List of 3 main discussion points"],
  "recommendations": ["List of actionable steps"]
}}
"""
from flask import Blueprint, request, jsonify
from services.groq_client import GroqClient
from services.prompt_manager import get_report_prompt

report_bp = Blueprint('report', __name__)
groq_client = GroqClient()

@report_bp.route('/generate-report', methods=['POST'])
def generate_report():
    data = request.json
    content = data.get('content', '')
    agenda = data.get('agenda', 'General Board Meeting')

    if not content:
        return jsonify({"error": "Content is required"}), 400

    prompt = get_report_prompt(content, agenda)
    
    try:
        response = groq_client.generate(prompt)
        return response, 200, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500
