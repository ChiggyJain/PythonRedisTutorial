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


def transaction_multi_exec_examples():
    try:

        print(f"Inside func: transaction_multi_exec_examples")
        global redisObj
        keyName = "Balance"
        redisObj.delete(keyName)

        pipeConObj = redisObj.pipeline(transaction=True)
        pipeConObj.set(keyName, 100)
        pipeConObj.incr(keyName)
        pipeConObj.incrby(keyName, 50)
        pipeConObj.get(keyName)
        results = pipeConObj.execute()
        print(f"Result from execute: {results}")
        print(f"Final Balance: {redisObj.get(keyName)}")
        


    except Exception as e:
        print(f"Exception occured inside func transaction_multi_exec_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    transaction_multi_exec_examples()

