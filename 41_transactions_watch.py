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


def deduct_amount(user, amount):
    keyName = "Account-Balance"
    while True:
        try:
            redisObj.watch(keyName)
            curBalance = int(redisObj.get(keyName))
            print(f"{user} current balance: {curBalance}")
            if curBalance<amount:
                print(f"{user} not have enough balance.")
                redisObj.unwatch(keyName)
                return
            newBalance = curBalance-amount
            pipe = redisObj.pipeline()
            pipe.multi()
            pipe.set(keyName, newBalance)
            results = pipe.execute()
            if results:
                print(f"{user} deducted {amount}. New balance: {newBalance}")
                break
            else:
                print(f"{user} conflicts deducted")
        except redis.WatchError:
            continue

def transaction_watch_examples():
    try:

        print(f"Inside func: transaction_watch_examples")
        global redisObj
        keyName = "Account-Balance"
        redisObj.delete(keyName)
        redisObj.set(keyName, 100)

        t1 = threading.Thread(target=deduct_amount, args=("User-A", 80))
        t2 = threading.Thread(target=deduct_amount, args=("User-B", 80))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(f"Final Balance: {redisObj.get(keyName)}")
        

    except Exception as e:
        print(f"Exception occured inside func transaction_watch_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    transaction_watch_examples()

