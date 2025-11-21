
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


def stream_basic_examples():
    try:

        print(f"Inside func: stream_basic_examples")
        global redisObj

        keyName1 = f"Event-Streams"
        redisObj.delete(keyName1)
        
        print(f"Adding events to stream")
        evntId = redisObj.xadd(keyName1, {"userId" : 11, "userName": "U1"})  
        print(f"Event-ID: {evntId}")
        evntId = redisObj.xadd(keyName1, {"userId" : 12, "userName": "U2"})  
        print(f"Event-ID: {evntId}")
        print(f"Reading all events from stream: {redisObj.xrange(keyName1, min="-", max="+")}")
        

    except Exception as e:
        print(f"Exception occured inside func stream_basic_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    stream_basic_examples()

