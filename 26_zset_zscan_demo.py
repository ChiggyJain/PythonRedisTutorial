
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


def zscan_examples():
    try:

        print(f"Inside func: zscan_examples")
        global redisObj

        keyName1 = f"Zscan-Demo"
        redisObj.delete(keyName1)
        
        # adding items to sorted set
        for i in range(1,10001):
            redisObj.zadd(keyName1, {f"User-ID:{i}" : i*10})
        
        print(f"Fetching all zsets in one short: {redisObj.zrange(keyName1, 0, -1, withscores=True)}")  
        print(f"Fetching all zsets in chunk by chunk")
        nxtCursor = 0
        while True:
            nxtCursor, items = redisObj.zscan(keyName1, cursor=nxtCursor, count=10)
            print(f"Batch-Items: {items}, NxtCursor: {nxtCursor}")
            if nxtCursor == 0:
                break


    except Exception as e:
        print(f"Exception occured inside func zscan_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    zscan_examples()

