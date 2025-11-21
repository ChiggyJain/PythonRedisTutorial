

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


def zsets_score_range_pop_examples():
    try:

        print(f"Inside func: zsets_score_range_pop_examples")
        global redisObj

        keyName1 = f"Scores"
        redisObj.delete(keyName1)
        
        # adding member with score
        redisObj.zadd(keyName1, {"C1" : 50})
        redisObj.zadd(keyName1, {"C2" : 120})
        redisObj.zadd(keyName1, {"C3" : 90})
        redisObj.zadd(keyName1, {"C4" : 200})
        redisObj.zadd(keyName1, {"C5" : 150})
        print(f"Fetching all zsets members by score ascending: {redisObj.zrange(keyName1, 0, -1, withscores=True)}")        
        print(f"Fetching all zsets members by score descending: {redisObj.zrevrange(keyName1, 0, -1, withscores=True)}")
        print(f"Fetching score of member(C1) from zsets: {redisObj.zscore(keyName1, "C1")}")
        print(f"Fetching rank of member(C2) from redis set as ascending order: {redisObj.zrank(keyName1, "C2")}")
        print(f"Fetching rank of member(C2) from redis set as descending order: {redisObj.zrevrank(keyName1, "C2")}")
        print(f"Incrementing score of member(C2) into redis : {redisObj.zincrby(keyName1, 10, "C2")}")
        print(f"Fetching all zsets members by score ascending: {redisObj.zrange(keyName1, 0, -1, withscores=True)}")
        print(f"Fetching all zsets members by score between 50 to 90: {redisObj.zrangebyscore(keyName1, 50, 90, withscores=True)}")
        print(f"Removing min-score members from sets: {redisObj.zpopmin(keyName1)}")
        print(f"Fetching all zsets members by score ascending: {redisObj.zrange(keyName1, 0, -1, withscores=True)}")     
        print(f"Removing max-score members from sets: {redisObj.zpopmax(keyName1)}")
        print(f"Fetching all zsets members by score ascending: {redisObj.zrange(keyName1, 0, -1, withscores=True)}")    

    except Exception as e:
        print(f"Exception occured inside func zsets_score_range_pop_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    zsets_score_range_pop_examples()
