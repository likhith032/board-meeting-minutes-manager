# AI Microservice - Board Meeting Manager
Powered by Flask & Groq (LLaMA 3.3)

## Setup
1. `pip install -r requirements.txt`
2. Create `.env` with `GROQ_API_KEY` and `REDIS_HOST`.
3. `python app.py`

## API Reference
- `POST /describe`: Generates meeting summary.
- `POST /recommend`: Extracts 3 action items.
- `GET /health`: System status & uptime.
