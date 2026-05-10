def get_report_prompt(content, agenda):
    return f"""
    Task: Create a formal Board Meeting Report.
    Agenda Context: {agenda}
    Raw Minutes: {content}
    
    Output: JSON object (title, summary, overview, key_items, recommendations).
    """
