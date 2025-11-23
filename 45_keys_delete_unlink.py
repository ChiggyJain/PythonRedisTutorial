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


def delete_unlink_examples():
    try:

        print(f"Inside func: delete_unlink_examples")
        global redisObj

        keyName = "Big-Key"
        redisObj.delete(keyName)
        for i in range(1, 10001):
            redisObj.rpush(keyName, i)
        print(f"Deleting-Big-Key: {redisObj.delete(keyName)}")

        keyName = "Big-Key"
        redisObj.delete(keyName)
        for i in range(1, 10001):
            redisObj.rpush(keyName, i)
        print(f"Deleting-Big-Key: {redisObj.unlink(keyName)}")

        

    except Exception as e:
        print(f"Exception occured inside func delete_unlink_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    delete_unlink_examples()

