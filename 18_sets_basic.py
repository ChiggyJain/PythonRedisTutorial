
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


def sets_basic_examples():
    try:

        print(f"Inside func: sets_basic_examples")
        global redisObj

        keyName = f"Log-Sets"
        redisObj.delete(keyName)
        logsList = ["Log-ID-1", "Log-ID-2", "Log-ID-1", "Log-ID-1", "Log-ID-3", "Log-ID-4", "Log-ID-5", "Log-ID-11", "Log-ID-11"]

        print(f"Inserting Logs into redis Set")
        for logId in logsList:
            redisObj.sadd(keyName, logId)
        print(f"Reading all logs from redis set: {redisObj.smembers(keyName)}")
        print(f"Count of all logs from redis set: {redisObj.scard(keyName)}")
        print(f"Checking (Log-ID-1) is exists into redis set: {redisObj.sismember(keyName, "Log-ID-1")}")
        redisObj.srem(keyName, "Log-ID-1")
        print(f"Reading all logs from redis set: {redisObj.smembers(keyName)}")
        
    except Exception as e:
        print(f"Exception occured inside func sets_basic_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    sets_basic_examples()
