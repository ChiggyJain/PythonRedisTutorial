
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


def stream_consumer_read_ack_examples():
    try:

        print(f"Inside func: stream_consumer_read_ack_examples")
        global redisObj

        streamName = f"Order-Stream"
        groupName = f"Order-Group"
        redisObj.delete(streamName)
        
        print(f"Adding events to stream")
        eventIdList = []
        for i in range(1, 6):
            eventId = redisObj.xadd(streamName, {"Order-ID" : f"{i}"})
            eventIdList.append(eventId)
        print(f"Generated Event-IDs: {eventIdList}")
        print(f"Reading all order from redis stream in ascending: {redisObj.xrange(streamName, min="-", max="+")}")

        # creating consumer-group into redis stream    
        redisObj.xgroup_create(streamName, groupName, id="0", mkstream=True)
        
        msgs = redisObj.xreadgroup(groupName, "Worker-1", {streamName:">"}, count=10)
        print("Messages for worker-1 and now status are pending after reading:", msgs)

        msgIdList = [msgId for msgId, _ in msgs[0][1]]
        print(f"All-Msg-IDs: {msgIdList}")
        print(f"Acknowledging each message now")
        for eachMsgId in msgIdList:
            ackStatus = redisObj.xack(streamName, groupName, eachMsgId)
            print(f"Msg-Id: {eachMsgId}, Ack-Status: {ackStatus}")

        pendingMsg = redisObj.xpending(streamName, groupName)
        print(f"Pending-Msg: {pendingMsg}")   


    except Exception as e:
        print(f"Exception occured inside func stream_consumer_read_ack_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    stream_consumer_read_ack_examples()

