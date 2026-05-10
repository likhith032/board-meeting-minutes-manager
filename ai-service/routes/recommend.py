@recommend_bp.route('/recommend', methods=['POST'])
def get_recommendations():
    try:
        data = request.json
        content = data.get('content')

        # Day 5 Task: Handle null/empty input gracefully
        if not content or len(content.strip()) == 0:
            return jsonify({
                "recommendations": [],
                "status": "empty_input",
                "message": "No content provided for analysis"
            }), 200 # Returning 200 with empty list so Java doesn't throw a 400 error

        # Call the client
        result = groq_client.generate(content)
        
        # Ensure result is not null before returning
        if result is None:
            return jsonify({"recommendations": [], "status": "ai_failure"}), 200

        return result, 200

    except Exception as e:
        # Graceful error handling for the async call from Java
        return jsonify({
            "recommendations": [], 
            "status": "error",
            "error_log": str(e)
        }), 200
