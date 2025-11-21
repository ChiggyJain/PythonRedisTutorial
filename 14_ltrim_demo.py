
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


def list_ltrim_operation_examples():
    try:

        print(f"Inside func: list_ltrim_operation_examples")
        global redisObj

        keyName = f"Log-List"
        redisObj.delete(keyName)

        print(f"Inserting 10-Logs into redis List from right side")
        for i in range(1, 11):
            redisObj.rpush(keyName, f"Log-ID:{i}")
        print(f"Reading all logs from redis list: {redisObj.lrange(keyName, 0, -1)}")    
        print(f"Applying ltrim to keep only 5 logs in list")
        redisObj.ltrim(keyName, 0, 4)
        print(f"Reading all logs from redis list after ltrim: {redisObj.lrange(keyName, 0, -1)}")

    except Exception as e:
        print(f"Exception occured inside func list_ltrim_operation_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    list_ltrim_operation_examples()
