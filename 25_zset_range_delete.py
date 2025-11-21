
import redis
from time import time
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


def zsets_range_delete_examples():
    try:

        print(f"Inside func: zsets_range_delete_examples")
        global redisObj

        keyName1 = f"Events"
        redisObj.delete(keyName1)
        curTime = int(time())
        
        # adding member with score
        redisObj.zadd(keyName1, {"Event1" : curTime-50})
        redisObj.zadd(keyName1, {"Event2" : curTime-40})
        redisObj.zadd(keyName1, {"Event3" : curTime-30})
        redisObj.zadd(keyName1, {"Event4" : curTime-20})
        redisObj.zadd(keyName1, {"Event5" : curTime-10})
        print(f"Fetching all zsets events by score ascending: {redisObj.zrange(keyName1, 0, -1, withscores=True)}")  
        print(f"Fetching all zsets events which is last in 30 seconds: {redisObj.zrangebyscore(keyName1, curTime-30, curTime, withscores=True)}")
        print(f"Fetching all zsets events which is last in 30 seconds and limit=1: {redisObj.zrangebyscore(keyName1, curTime-30, curTime, 1, 1, withscores=True)}")  
        print(f"Deleting all zsets events which is last in 30 seconds: {redisObj.zremrangebyscore(keyName1, curTime-30, curTime)}")
        print(f"Fetching all zsets events by score ascending: {redisObj.zrange(keyName1, 0, -1, withscores=True)}")

    except Exception as e:
        print(f"Exception occured inside func zsets_range_delete_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    zsets_range_delete_examples()
