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


def rdb_persistent_examples():
    try:

        print(f"Inside func: rdb_persistent_examples")
        global redisObj

        keyName = "Initial-Stock"
        redisObj.delete(keyName)
        redisObj.set(keyName, 3)

        result = redisObj.bgsave()
        print(f"Result: {result}")
        print(f"Last-Save-Time: {redisObj.lastsave()}")

        

    except Exception as e:
        print(f"Exception occured inside func rdb_persistent_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    rdb_persistent_examples()

