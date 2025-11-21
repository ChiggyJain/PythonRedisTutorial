
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


def worker_examples():
    try:

        print(f"Inside func: worker_examples")
        global redisObj

        job_queue_key = f"Job_Queue"
        while True:
            item = redisObj.brpop(job_queue_key)
            if item:
                job_queue_name, job_queue_raw_data = item
                print(f"Received job from {job_queue_name}: {json.loads(job_queue_raw_data)}")

    except Exception as e:
        print(f"Exception occured inside func worker_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    worker_examples()