
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


def sets_random_examples():
    try:

        print(f"Inside func: sets_random_examples")
        global redisObj

        keyName1 = f"Log-Sets-1"
        redisObj.delete(keyName1)
        
        logsList1 = ["Log-ID-1", "Log-ID-2", "Log-ID-1", "Log-ID-1", "Log-ID-3", "Log-ID-4", "Log-ID-5", "Log-ID-11", "Log-ID-11"]

        print(f"Inserting Logs1 into redis Set")
        for logId in logsList1:
            redisObj.sadd(keyName1, logId)
        print(f"Reading all Logs1 from redis set: {redisObj.smembers(keyName1)}")
        print(f"Getting random logs from redis sets: {redisObj.srandmember(keyName1, number=2)}")
        print(f"Removing random logs from redis sets: {redisObj.spop(keyName1, count=2)}")
        print(f"Reading all Logs1 from redis set: {redisObj.smembers(keyName1)}")
        
    except Exception as e:
        print(f"Exception occured inside func sets_random_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    sets_random_examples()
