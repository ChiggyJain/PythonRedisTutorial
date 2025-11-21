
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


def list_lpos_examples():
    try:

        print(f"Inside func: list_lpos_examples")
        global redisObj

        keyName = f"Log-List"
        redisObj.delete(keyName)
        logsList = ["Log-ID-1", "Log-ID-2", "Log-ID-1", "Log-ID-1", "Log-ID-3", "Log-ID-4", "Log-ID-5", "Log-ID-11", "Log-ID-11"]

        print(f"Inserting Logs into redis List from right side")
        for logId in logsList:
            redisObj.rpush(keyName, logId)
        print(f"Reading all logs from redis list: {redisObj.lrange(keyName, 0, -1)}")
        print(f"Searching (Log-ID-2) in redis list and returning first occurence indexes: {redisObj.lpos(keyName, "Log-ID-2")}")
        print(f"Searching (Log-ID-1) in redis list via Rank=3 occurence and return indexes: {redisObj.lpos(keyName, "Log-ID-1", rank=3)}")
        print(f"Finding (Log-ID-1) in redis list via count=3 and return occurence indexes: {redisObj.lpos(keyName, "Log-ID-1", count=3)}")
        print(f"Finding (Log-ID-2) in redis list via maxlen=3 and return occurence indexes: {redisObj.lpos(keyName, "Log-ID-2", maxlen=3)}")

    except Exception as e:
        print(f"Exception occured inside func list_lpos_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    list_lpos_examples()
