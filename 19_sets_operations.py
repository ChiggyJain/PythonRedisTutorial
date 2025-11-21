
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


def sets_operation_examples():
    try:

        print(f"Inside func: sets_operation_examples")
        global redisObj

        keyName1 = f"Log-Sets-1"
        redisObj.delete(keyName1)
        keyName2 = f"Log-Sets-2"
        redisObj.delete(keyName2)

        logsList1 = ["Log-ID-1", "Log-ID-2", "Log-ID-1", "Log-ID-1", "Log-ID-3", "Log-ID-4", "Log-ID-5", "Log-ID-11", "Log-ID-11"]
        logsList2 = ["Log-ID-1", "Log-ID-2", "Log-ID-1", "Log-ID-1", "Log-ID-3", "Log-ID-4", "Log-ID-5", "Log-ID-11", "Log-ID-11", "Log-ID-12"]

        print(f"Inserting Logs1 into redis Set")
        for logId in logsList1:
            redisObj.sadd(keyName1, logId)
        print(f"Reading all Logs1 from redis set: {redisObj.smembers(keyName1)}")

        print(f"Inserting Logs2 into redis Set")
        for logId in logsList2:
            redisObj.sadd(keyName2, logId)
        print(f"Reading all Logs2 from redis set: {redisObj.smembers(keyName2)}")

        print(f"Union unique logs from logs(Logs1, Logs2): {redisObj.sunion(keyName1, keyName2)}")
        print(f"Intersection logs from logs(Logs1, Logs2): {redisObj.sinter(keyName1, keyName2)}")
        print(f"Difference logs from logs(Logs2, Logs1): {redisObj.sdiff(keyName2, keyName1)}")
        
    except Exception as e:
        print(f"Exception occured inside func sets_operation_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    sets_operation_examples()
