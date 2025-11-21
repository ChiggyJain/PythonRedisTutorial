
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


def list_lrem_linsert_examples():
    try:

        print(f"Inside func: list_lrem_linsert_examples")
        global redisObj

        keyName = f"Log-List"
        redisObj.delete(keyName)
        logsList = ["Log-ID-1", "Log-ID-2", "Log-ID-3", "Log-ID-4", "Log-ID-5", "Log-ID-11", "Log-ID-11"]

        print(f"Inserting 7-Logs into redis List from right side")
        for logId in logsList:
            redisObj.rpush(keyName, logId)
        print(f"Reading all logs from redis list: {redisObj.lrange(keyName, 0, -1)}")
        print(f"Removing log (Log-ID-11) from redis list and return total-element-removed: {redisObj.lrem(keyName, 0, "Log-ID-11")}")
        print(f"Reading all logs from redis list: {redisObj.lrange(keyName, 0, -1)}")
        print(f"Inserting log (Log-ID-11) into redis list after Log-ID-5")
        redisObj.linsert(keyName, "AFTER", "Log-ID-5", "Log-ID-11")
        print(f"Reading all logs from redis list: {redisObj.lrange(keyName, 0, -1)}")
        redisObj.linsert(keyName, "BEFORE", "Log-ID-5", "Log-ID-11")
        print(f"Reading all logs from redis list: {redisObj.lrange(keyName, 0, -1)}")

    except Exception as e:
        print(f"Exception occured inside func list_lrem_linsert_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    list_lrem_linsert_examples()
