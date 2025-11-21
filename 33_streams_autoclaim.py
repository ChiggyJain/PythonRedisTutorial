
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


def stream_consumer_autoclaim_examples():
    try:

        print(f"Inside func: stream_consumer_autoclaim_examples")
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

        # creating consumer-group into redis stream    
        redisObj.xgroup_create(streamName, groupName, id="0", mkstream=True)
        
        worker1_msgs = redisObj.xreadgroup(groupName, "Worker-1", {streamName:">"}, count=5)
        print("Messages for worker-1 and now status are pending after reading:", worker1_msgs)

        worker2_msgs = redisObj.xreadgroup(groupName, "Worker-2", {streamName:">"}, count=5)
        print("Messages for worker-2 and now status are pending after reading:", worker2_msgs)

        print(f"Pending-Msg-Summary: {redisObj.xpending(streamName, groupName)}")
        print(f"Pending-Msg-Details: {redisObj.xpending_range(streamName, groupName, "-", "+", 1000)}")

        time.sleep(2)

        print(f"Now Worker-3 tries to autoclaim all messages from Worker-1, Worker-2 which is stuck greater than 1 seconds")
        newCursor, claimed, deleted = redisObj.xautoclaim(streamName, groupName, "Worker-3", min_idle_time=1000, count=1000)
        print(f"New-Cursor: {newCursor}")
        print(f"Claimed: {claimed}")
        print(f"Deleted: {deleted}")
        print(f"Pending-Msg-Summary: {redisObj.xpending(streamName, groupName)}")
           


    except Exception as e:
        print(f"Exception occured inside func stream_consumer_autoclaim_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    stream_consumer_autoclaim_examples()

