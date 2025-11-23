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


def pipeline_examples():
    try:

        print(f"Inside func: pipeline_examples")
        global redisObj

        print(f"Without pipeline-demo")
        startTime = time.time()
        for i in range(1, 10001):
            redisObj.set(f"Without-Pipeline-Key-{i}", i)
        print(f"Total-Time: {time.time()-startTime}")

        print(f"With pipeline-demo")
        pipe = redisObj.pipeline(transaction=False)
        for i in range(1, 10001):
            pipe.set(f"With-Pipeline-Key-{i}", i)
        pipe.execute()
        print(f"Total-Time: {time.time()-startTime}")


    except Exception as e:
        print(f"Exception occured inside func pipeline_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    pipeline_examples()

