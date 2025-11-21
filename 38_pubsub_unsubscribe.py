import redis
import time
import threading
redisObj = None
pubSubConObj = None


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
    global redisObj, pubSubConObj
    pubSubConObj = redisObj.pubsub()
    pubSubConObj.psubscribe(channelName)
    print(f"{subscriberName} is subscribe to channel {channelName}")
    for msg in pubSubConObj.listen():
        if msg["type"] == "message":
            print(f"{subscriberName} is message-received msg {msg} from channel {channelName}")
        if msg["type"] == "pmessage":
            print(f"{subscriberName} is pmessage-received msg {msg} from channel {channelName}")
        if msg["type"] == "unsubscribe":
            print(f"{subscriberName} is unsubscribe-received msg {msg} from channel {channelName}")        


def publisherDemo(channelName):
    print(f"Inside func: publisherDemo")
    global redisObj
    redisObj.publish(channelName, "Match Started!")
    time.sleep(1)
    redisObj.publish(channelName, "Goal Scored!")
    time.sleep(1)


def pubsub_unsubscribe_examples():
    try:

        print(f"Inside func: pubsub_unsubscribe_examples")
        global redisObj, pubSubConObj
        channelName = "Sports.Live"

        # subscriber subscribing to the channel
        threading.Thread(target=subscriberDemo, args=(channelName, "Subsriber-1")).start()
        time.sleep(1)

        # publisher publishing the messages to channel
        publisherDemo(channelName)

        # subscriber un-subscribe from the channel
        pubSubConObj.unsubscribe(channelName)


    except Exception as e:
        print(f"Exception occured inside func pubsub_unsubscribe_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    pubsub_unsubscribe_examples()

