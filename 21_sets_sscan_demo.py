
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


def sets_sscan_examples():
    try:

        print(f"Inside func: sets_sscan_examples")
        global redisObj

        keyName1 = f"Log-Sets-1"
        redisObj.delete(keyName1)
        
        print(f"Inserting 100-Logs into redis Set")
        for logId in range(1, 101):
            redisObj.sadd(keyName1, f"Log-ID:{logId}")
        print(f"Reading all Logs from redis set in a single shot: {redisObj.smembers(keyName1)}")
        print("Scanning large set using SSCAN")
        nextCursor = 0
        while True:
            nextCursor, items = redisObj.sscan(keyName1, cursor=nextCursor, count=10)
            print(f"Fetched-Items: {items}, Next-Cursor: {nextCursor}")
            if nextCursor == 0:
                break

    except Exception as e:
        print(f"Exception occured inside func sets_sscan_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    sets_sscan_examples()
