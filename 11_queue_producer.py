
import redis
import json
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


def producer_examples():
    try:

        print(f"Inside func: producer_examples")
        global redisObj


        # deleting all tasks from list as queue [FIFO]
        job_queue_key = f"Job_Queue"
        redisObj.delete(job_queue_key)
        
        for i in range(1, 6):
            job = {"job_id": i, "task": f"process_{i}"}
            redisObj.lpush(job_queue_key, json.dumps(job))
            print(f"Job is pushed into redis queue-list: {job}")

    except Exception as e:
        print(f"Exception occured inside func producer_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    producer_examples()