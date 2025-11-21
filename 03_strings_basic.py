
import redis
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


def redis_string_datatypes_examples():
    print(f"Inside func: redis_string_datatypes_examples")
    global redisObj
    
    redisObj.set("User:FullName", "Chirag Jain")
    print(f"Getting User:FullName from redis: {redisObj.get("User:FullName")}")

    redisObj.set("User-ID-OTP:11", "123456", ex=300)
    print(f"Getting User-ID-OTP:11 from redis: {redisObj.get("User-ID-OTP:11")}")

    redisObj.set("Product-Page-View-Count", 0)
    redisObj.incr("Product-Page-View-Count")
    redisObj.incr("Product-Page-View-Count")
    redisObj.incr("Product-Page-View-Count")
    print(f"Getting total count of product page view from redis: {redisObj.get("Product-Page-View-Count")}")

    redisObj.set("Storing-Mobile-Nos", "12")
    redisObj.append("Storing-Mobile-Nos", "13")
    redisObj.append("Storing-Mobile-Nos", "14")
    print(f"Getting all user-mobile-numbers from redis: {redisObj.get("Storing-Mobile-Nos")}")


if __name__ == "__main__":
    make_redis_connection()
    redis_string_datatypes_examples()