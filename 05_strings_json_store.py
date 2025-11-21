

import redis
import json
redisObj = None


def make_redis_connection():
    print(f"Inside func: make_redis_connection")
    try:
        global redisObj
        redisObj = redis.Redis(host="localhost", port=6379, decode_responses=True)
        pong = redisObj.ping()
        print(f"Redis connected successfully: {pong}")
    except Exception as e:
        print(f"Exception occured inside func: make_redis_connection => {e}")


def redis_string_datatypes_json_examples():
    print(f"Inside func: redis_string_datatypes_json_examples")
    global redisObj
    
    userInfo = {
        "userId" : 11,
        "userFullName" : "Chirag D Jain"
    }
    redisObj.set("User-ID:11", json.dumps(userInfo))
    print(f"Stored user-info-json-information in redis")
    print(f"Extracted user-info-json from redis as raw-string: {redisObj.get("User-ID:11")}")


if __name__ == "__main__":
    make_redis_connection()
    redis_string_datatypes_json_examples()