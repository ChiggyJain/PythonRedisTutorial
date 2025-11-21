import redis
import time
import threading
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


def subscriberDemo(channelName, subscriberName):
    print(f"Inside func: subscriberDemo")
    global redisObj
    pubSubConObj = redisObj.pubsub()
    pubSubConObj.psubscribe(channelName)
    print(f"{subscriberName} is subscribe to channel {channelName}")
    for msg in pubSubConObj.listen():
        if msg["type"] == "message" or msg["type"] == "pmessage":
            print(f"{subscriberName} is received msg {msg} from channel {channelName}")


def publisherDemo():
    
    print(f"Inside func: publisherDemo")
    global redisObj

    time.sleep(1)
    redisObj.publish("Chat.Room1", "Hello-Everyone-Chat.Room1")

    time.sleep(1)
    redisObj.publish("Chat.Room2", "Hello-Everyone-Chat.Room2")

    time.sleep(1)
    redisObj.publish("Chat.Room3", "Hello-Everyone-Chat.Room3")


def pubsub_pattern_examples():
    try:

        print(f"Inside func: pubsub_examples")
        global redisObj
        channelNamePattern = "Chat.*"

        threading.Thread(target=subscriberDemo, args=(channelNamePattern, "Subsriber-1"), daemon=False).start()
        threading.Thread(target=subscriberDemo, args=(channelNamePattern, "Subsriber-2"), daemon=False).start()

        publisherDemo()

    except Exception as e:
        print(f"Exception occured inside func pubsub_pattern_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    pubsub_pattern_examples()

