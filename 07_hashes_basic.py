

import redis
import json
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


def redis_hash_basic_examples():
    try:

        print(f"Inside func: redis_hash_basic_examples")
        global redisObj
        
        redisObj.hset("User-ID-111", mapping={
            "userId" : "111",
            "userFullName" : "Chirag D Jain",
            "userRole" : "Developer"
        })
        print(f"Reading full hash from redis using key:User-ID-111: {redisObj.hgetall("User-ID-111")}")
        print(f"Reading specific-key hash from redis using key:User-ID-111: {redisObj.hget("User-ID-111", "userFullName")}")
        redisObj.hset("User-ID-111", "userRole", "Backend Engineer")
        print(f"Reading full hash from redis using key:User-ID-111: {redisObj.hgetall("User-ID-111")}")

    except Exception as e:
        print(f"Exception occured inside func redis_hash_basic_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    redis_hash_basic_examples()