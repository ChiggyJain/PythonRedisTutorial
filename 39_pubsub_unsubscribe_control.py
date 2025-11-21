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


def subscriberDemo(mainChannelName, controlChannelName, subscriberName):
    print(f"Inside func: subscriberDemo")
    global redisObj, pubSubConObj
    pubSubConObj = redisObj.pubsub()
    pubSubConObj.subscribe(mainChannelName)
    pubSubConObj.subscribe(controlChannelName)
    print(f"{subscriberName} is subscribe to main-channel: {mainChannelName}")
    print(f"{subscriberName} is subscribe to control-channel: {controlChannelName}")

    for msg in pubSubConObj.listen():
        #print(f"Received-Msg: {msg}")
        if msg["type"] == "message" and msg["channel"] == mainChannelName:
            print(f"{subscriberName} message-received msg: {msg} from channel: {mainChannelName}")
        if msg["type"] == "message" and msg["channel"] == controlChannelName:
            command = msg["data"]
            if command == "STOP":
                print(f"Control channel command received by subscriber: {command}")
                pubSubConObj.unsubscribe(mainChannelName)
                pubSubConObj.unsubscribe(controlChannelName)
                pubSubConObj.close()
                print(f"{subscriberName} unsubscribe-received msg: {msg} from main-channel: {mainChannelName}")
                print(f"{subscriberName} unsubscribe-received msg: {msg} from control-channel: {controlChannelName}")
                break        


def publisherDemo(mainChannelName, controlChannelName):
    print(f"Inside func: publisherDemo")
    global redisObj
    print(f"Publisher publishing messages to main-channel: {mainChannelName}")
    redisObj.publish(mainChannelName, "Match Started!")
    time.sleep(1)
    redisObj.publish(controlChannelName, "Goal Scored!")
    time.sleep(1)
    print(f"Publisher publishing messages to control-channel for un-subscribe the channel: {controlChannelName}")
    redisObj.publish(controlChannelName, "STOP")



def pubsub_unsubscribe_control_examples():
    try:

        print(f"Inside func: pubsub_unsubscribe_control_examples")
        global redisObj, pubSubConObj
        mainChannelName = "Sports.Live"
        controlChannelName = "Sports.Live"

        # subscriber subscribing to the channel
        threading.Thread(target=subscriberDemo, args=(mainChannelName, controlChannelName, "Subsriber-1")).start()
        time.sleep(1)

        # publisher publishing the messages to channel
        publisherDemo(mainChannelName, controlChannelName)


    except Exception as e:
        print(f"Exception occured inside func pubsub_unsubscribe_control_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    pubsub_unsubscribe_control_examples()

