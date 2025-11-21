
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


def redis_string_datatypes_increment_counter_examples():
    print(f"Inside func: redis_string_datatypes_increment_examples")
    global redisObj
    
    redisObj.set("User-ID-Login-Attempt:11", 0)
    redisObj.incr("User-ID-Login-Attempt:11")
    redisObj.incr("User-ID-Login-Attempt:11")
    redisObj.incr("User-ID-Login-Attempt:11")
    print(f"From redis total-login-attempt-count: {redisObj.get("User-ID-Login-Attempt:11")} for User-ID-Login-Attempt:11")
    print(f"Now incrementing login-attempt by 5")
    redisObj.incrby("User-ID-Login-Attempt:11", 5)
    print(f"From redis total-login-attempt-count: {redisObj.get("User-ID-Login-Attempt:11")} for User-ID-Login-Attempt:11")
    

if __name__ == "__main__":
    make_redis_connection()
    redis_string_datatypes_increment_counter_examples()