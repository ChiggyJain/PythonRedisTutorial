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


def ttl_expire_examples():
    try:

        print(f"Inside func: ttl_expire_examples")
        global redisObj

        keyName = "Temp-User-Session"
        redisObj.set(keyName, "Active")
        redisObj.expire(keyName, 5)
        for i in range(6):
            ttl = redisObj.ttl(keyName)
            print(f"keyName: {keyName}, Second {i}: TTL = {ttl}")
            time.sleep(1)

        keyName = "Temp-User-Session"
        redisObj.set(keyName, "Active")
        redisObj.pexpire(keyName, 5000)
        for i in range(6):
            ttl = redisObj.pttl(keyName)
            print(f"keyName:{keyName}, Second {i}: TTL = {ttl}")
            time.sleep(1)

    except Exception as e:
        print(f"Exception occured inside func ttl_expire_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    ttl_expire_examples()

