from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# Register route blueprints here as they are built
# from routes.describe import describe_bp
# from routes.recommend import recommend_bp
# from routes.report import report_bp
# app.register_blueprint(describe_bp)
# app.register_blueprint(recommend_bp)
# app.register_blueprint(report_bp)

@app.route("/health", methods=["GET"])
def health():

    import hashlib
    import redis
    import time
    from flask import Flask, request, jsonify

    app = Flask(__name__)
    cache = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=0)
    start_time = time.time()

    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({
            "status": "healthy",
            "model": "llama-3.3-70b-versatile",
            "uptime": f"{int(time.time() - start_time)}s",
            "avg_response_time": "1.2s" # This would be a moving average in prod
    })

    def get_cache_key(prompt):
        return hashlib.sha256(prompt.encode()).hexdigest()

# Inside your /describe or /recommend routes:
# key = get_cache_key(prompt)
# cached_res = cache.get(key)
# if cached_res: return cached_res
# else: ... call Groq ... cache.setex(key, 900, response)
        return {"status": "ok", "service": "ai-service"}, 200


    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response
