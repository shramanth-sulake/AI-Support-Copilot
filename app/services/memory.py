from app.db.redis import redis_client
import json

def save_message(session_id: str, role: str, content: str):
    key = f"chat:{session_id}"

    message = {
        "role": role,
        "content": content
    }

    redis_client.rpush(key, json.dumps(message))

    # keep only last 10 messages
    redis_client.ltrim(key, -10, -1)


def get_history(session_id: str):
    key = f"chat:{session_id}"

    messages = redis_client.lrange(key, 0, -1)

    return [json.loads(m) for m in messages]