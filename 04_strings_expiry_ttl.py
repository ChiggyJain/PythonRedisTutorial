
import redis
import time
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


def redis_string_datatypes_expiry_ttl_examples():
    print(f"Inside func: redis_string_datatypes_expiry_ttl_examples")
    global redisObj
    
    
    redisObj.set("User-ID-OTP:11", "123456", ex=5)
    print(f"TTL set: {redisObj.ttl("User-ID-OTP:11")} seconds for User-ID-OTP:11 and Value is 123456")
    time.sleep(2)
    print(f"After 2 seconds TTL is still-available-in-seconds: {redisObj.ttl("User-ID-OTP:11")} for User-ID-OTP:11 and Value is 123456")
    time.sleep(6)
    print(f"OTP-Value: {redisObj.get("User-ID-OTP:11")} for User-ID-OTP:11 afte expiry TTL")


if __name__ == "__main__":
    make_redis_connection()
    redis_string_datatypes_expiry_ttl_examples()