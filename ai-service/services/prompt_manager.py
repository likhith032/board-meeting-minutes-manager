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
