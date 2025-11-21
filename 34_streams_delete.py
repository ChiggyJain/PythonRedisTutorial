
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


def stream_trim_examples():
    try:

        print(f"Inside func: stream_trim_examples")
        print(redis.__version__)
        global redisObj

        streamName = f"Order-Stream"
        groupName = f"Order-Group"
        redisObj.delete(streamName)
        
        print(f"Adding events to stream")
        eventIdList = []
        for i in range(1, 11):
            eventId = redisObj.xadd(streamName, {"Order-ID" : f"{i}"})
            eventIdList.append(eventId)
        print(f"Generated Event-IDs: {eventIdList}")
        print(f"Reading all order from redis stream in ascending: {redisObj.xrange(streamName, min="-", max="+")}")

        ## deleting specific messages by Id
        redisObj.xdel(streamName, eventIdList[0])
        print(f"Reading all order from redis stream in ascending: {redisObj.xrange(streamName, min="-", max="+")}")

        ## keeping last 3 messages only
        availableMsg = redisObj.xtrim(streamName, maxlen=3, approximate=False)
        print(f"Keeping only Last 3-Messages: {availableMsg}")
        print(f"Reading all order from redis stream in ascending: {redisObj.xrange(streamName, min="-", max="+")}")

    except Exception as e:
        print(f"Exception occured inside func stream_trim_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    stream_trim_examples()

