

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


def zsets_basic_examples():
    try:

        print(f"Inside func: zsets_basic_examples")
        global redisObj

        keyName1 = f"Leader-Board"
        redisObj.delete(keyName1)
        
        # adding member with score
        redisObj.zadd(keyName1, {"C1" : 101})
        redisObj.zadd(keyName1, {"C2" : 102})
        redisObj.zadd(keyName1, {"C3" : 105})
        redisObj.zadd(keyName1, {"C4" : 104})
        redisObj.zadd(keyName1, {"C5" : 103})
        print(f"Fetching all zsets members by score ascending: {redisObj.zrange(keyName1, 0, -1, withscores=True)}")
        print(f"Fetching all zsets members by score descending: {redisObj.zrevrange(keyName1, 0, -1, withscores=True)}")
        print(f"Fetching score of member(C1) from zsets: {redisObj.zscore(keyName1, "C1")}")
        print(f"Removing member(C1) from zsets: {redisObj.zrem(keyName1, "C1")}")
        print(f"Fetching all zsets members by score ascending: {redisObj.zrange(keyName1, 0, -1, withscores=True)}")


    except Exception as e:
        print(f"Exception occured inside func zsets_basic_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    zsets_basic_examples()
