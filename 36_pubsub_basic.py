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
    pubSubConObj.subscribe(channelName)
    print(f"{subscriberName} is subscribe to channel {channelName}")
    for msg in pubSubConObj.listen():
        if msg["type"] == "message":
            print(f"{subscriberName} is received msg {msg} from channel {channelName}")


def publisherDemo(channelName):
    
    print(f"Inside func: publisherDemo")
    global redisObj

    time.sleep(1)
    redisObj.publish(channelName, "Hello Everyone")

    time.sleep(1)
    redisObj.publish(channelName, "Welcome to Pub/Sub Tutorial")

    time.sleep(1)
    redisObj.publish(channelName, "This is real-time messaging")


def pubsub_examples():
    try:

        print(f"Inside func: pubsub_examples")
        global redisObj
        channelName = "Channel-1"

        threading.Thread(target=subscriberDemo, args=(channelName, "Subsriber-1"), daemon=False).start()
        threading.Thread(target=subscriberDemo, args=(channelName, "Subsriber-2"), daemon=False).start()

        publisherDemo(channelName)

    except Exception as e:
        print(f"Exception occured inside func pubsub_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    pubsub_examples()

