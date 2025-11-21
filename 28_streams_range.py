
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


def stream_range_examples():
    try:

        print(f"Inside func: stream_range_examples")
        global redisObj

        keyName1 = f"Event-Stream-Range"
        redisObj.delete(keyName1)
        
        print(f"Adding events to stream")
        eventIdList = []
        for i in range(1, 11):
            eventId = redisObj.xadd(keyName1, {"Event" : f"Event_{i}"})
            eventIdList.append(eventId)
            time.sleep(0.1)
        print(f"Generated Event-IDs: {eventIdList}")
        print(f"Reading all events from redis stream in ascending: {redisObj.xrange(keyName1, min="-", max="+")}")
        print(f"Reading all events from redis stream in ascending using given range: {redisObj.xrange(keyName1, eventIdList[2], eventIdList[4])}")
        print(f"Reading all events from redis stream in descending: {redisObj.xrevrange(keyName1, max="+", min="-")}")
        print(f"Reading last-3-events from redis stream in descending: {redisObj.xrevrange(keyName1, max="+", min="-", count=3)}")



    except Exception as e:
        print(f"Exception occured inside func stream_range_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    stream_range_examples()

