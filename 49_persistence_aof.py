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


def aof_persistent_examples():
    try:

        print(f"Inside func: aof_persistent_examples")
        global redisObj

        keyName = "Initial-Stock"
        redisObj.delete(keyName)
        redisObj.set(keyName, 3)

        print(f"AOF Enabled: {redisObj.info("persistence")["aof_enabled"]}")
        print("AOF file size (bytes):", redisObj.info("persistence"))
        result = redisObj.bgrewriteaof()
        # print("AOF new file size (bytes):", redisObj.info("persistence")["aof_current_size"])
        print("Rewrite triggered:", result)

    except Exception as e:
        print(f"Exception occured inside func aof_persistent_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    aof_persistent_examples()

