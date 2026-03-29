import redis
from fastapi import Request, HTTPException

try:
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.ping()
except:
    r = None   # fallback if Redis not available

RATE_LIMIT = 5
TIME_WINDOW = 60

def check_rate_limit(request: Request):
    if not r:
        return  # skip rate limit if Redis not available

    client_ip = request.client.host
    key = f"rate:{client_ip}"

    current = r.get(key)

    if current and int(current) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests 🚫")

    r.incr(key)

    if not current:
        r.expire(key, TIME_WINDOW)