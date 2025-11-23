import redis
import time
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


def scan_examples():
    try:

        print(f"Inside func: scan_examples")
        global redisObj

        for i in range(1, 10001):
            redisObj.set(f"Key#{i}", i)
        print(f"Using scan concept")
        nxtCursor = 0
        while True:
            nxtCursor, keys = redisObj.scan(cursor=nxtCursor, match="Key#*", count=10)
            print(f"NxtCursor: {nxtCursor} | Keys: {keys}")
            if nxtCursor == 0:
                break
        

    except Exception as e:
        print(f"Exception occured inside func scan_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    scan_examples()

