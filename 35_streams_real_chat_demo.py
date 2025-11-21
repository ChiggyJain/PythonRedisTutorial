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


def stream_chat_examples():
    try:

        print(f"Inside func: stream_chat_examples")
        print(redis.__version__)
        global redisObj

        streamName = f"Chat-Stream"
        groupName = f"Chat-Group"
        redisObj.delete(streamName)
        
        print(f"Creating chat-stream and chat-group")
        redisObj.xgroup_create(streamName, groupName, id="0", mkstream=True)

        ### sender sending msg
        msgId = redisObj.xadd(streamName, {"Sender":"C1", "Msg":"H1"})
        print(f"[SEND] C1:H1, Msg-ID: {msgId}")
        time.sleep(0.1)
        msgId = redisObj.xadd(streamName, {"Sender":"C2", "Msg":"H2"})
        print(f"[SEND] C2:H2, Msg-ID: {msgId}")
        time.sleep(0.1)
        msgId = redisObj.xadd(streamName, {"Sender":"C3", "Msg":"H3"})
        print(f"[SEND] C3:H3, Msg-ID: {msgId}")
        time.sleep(0.1)

        ## worker reading msg
        w1Streams = redisObj.xreadgroup(groupName, "Worker-1", {streamName:">"}, count=10)
        print(f"Worker-1 reading all msg and acknowledgeing: {w1Streams}")
        for msgId, msgData in w1Streams[0][1]:
            ackStatus = redisObj.xack(streamName, groupName, msgId)
            print(f"Worker-1 is ack to Msg-ID: {msgId}")


        ## worker reading msg
        w1Streams = redisObj.xreadgroup(groupName, "Worker-2", {streamName:">"}, count=10)
        print(f"Worker-2 reads msg: {w1Streams}")


    except Exception as e:
        print(f"Exception occured inside func stream_chat_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    stream_chat_examples()

