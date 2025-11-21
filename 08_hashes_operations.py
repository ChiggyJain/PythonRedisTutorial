

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


def redis_hash_operations_examples():
    try:

        print(f"Inside func: redis_hash_operations_examples")
        global redisObj
        
        redisObj.hset("User-ID-112", mapping={
            "userId" : "112",
            "userFullName" : "Chirag D Jain",
            "userRole" : "Developer"
        })
        print(f"Reading full hash-set-mapp from redis using key:User-ID-112: {redisObj.hgetall("User-ID-112")}")        
        print(f"Reading specific-field [userFullName] value from redis using hash-set-map key:User-ID-112: {redisObj.hget("User-ID-112", "userFullName")}")
        print(f"Reading fields [userFullName, Role] value from redis using hash-set-map key:User-ID-112: {redisObj.hmget("User-ID-112", ["userFullName", "userRole"])}")
        print(f"Checking field [userFullName] exists or not from redis using hash-set-map key:User-ID-112: {redisObj.hexists("User-ID-112", "userFullName")}")
        print(f"Deleting field [userRole] from redis using hash-set-map key:User-ID-112: {redisObj.hdel("User-ID-112", "userRole")}")
        print(f"Reading full hash-set-mapp from redis using key:User-ID-112: {redisObj.hgetall("User-ID-112")}")

    except Exception as e:
        print(f"Exception occured inside func redis_hash_operations_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    redis_hash_operations_examples()