from flask import Blueprint, request, jsonify
from services.groq_client import GroqClient
from services.prompt_manager import get_report_prompt # You'll add this next

report_bp = Blueprint('report', __name__)
groq_client = GroqClient()

@report_bp.route('/generate-report', methods=['POST'])
def generate_report():
    data = request.json
    content = data.get('content', '')
    agenda = data.get('agenda', 'Not provided')

    if not content:
        return jsonify({"error": "Meeting content is required"}), 400

    # Building the complex prompt
    prompt = f"""
    Generate a full, structured board report based on these minutes.
    Agenda: {agenda}
    Content: {content}

    Return ONLY a JSON object with these exact keys:
    {{
      "title": "Professional Report Title",
      "summary": "High-level executive summary (2 sentences)",
      "overview": "Detailed overview of discussions",
      "key_items": ["List of 3-5 main discussion points"],
      "recommendations": ["List of actionable steps"]
    }}
    """
    
    try:
        # Utilizing the GroqClient logic with retry/parsing
        report_json = groq_client.generate(prompt)
        return report_json, 200, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": f"Report generation failed: {str(e)}"}), 500
