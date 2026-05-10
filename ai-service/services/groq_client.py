def generate_with_fallback(self, prompt):
    try:
        return self.generate(prompt)
    except Exception:
        return {
            "is_fallback": True,
            "summary": "AI Service is temporarily unavailable. Please review manually.",
            "recommendations": ["Review meeting minutes for urgent actions."]
        }
