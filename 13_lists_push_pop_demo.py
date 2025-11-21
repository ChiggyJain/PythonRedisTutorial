
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


def list_all_operation_examples():
    try:

        print(f"Inside func: list_all_operation_examples")
        global redisObj

        keyName = f"Demo-Key"
        redisObj.delete(keyName)

        print(f"LPUSH concept")
        redisObj.lpush(keyName, "A")
        redisObj.lpush(keyName, "B")
        print(f"After LPUSH: B,A: {redisObj.lrange(keyName, 0, -1)}")

        print(f"RPUSH concept")
        redisObj.rpush(keyName, "C")
        redisObj.rpush(keyName, "D")
        print(f"After RPUSH: B,A,C,D: {redisObj.lrange(keyName, 0, -1)}")

        print(f"LPOP Element: {redisObj.lpop(keyName)}")
        print(f"Remaining List: {redisObj.lrange(keyName, 0, -1)}")

        print(f"RPOP Element: {redisObj.rpop(keyName)}")
        print(f"Remaining List: {redisObj.lrange(keyName, 0, -1)}")

    except Exception as e:
        print(f"Exception occured inside func list_all_operation_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    list_all_operation_examples()