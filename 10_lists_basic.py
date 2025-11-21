

import redis
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


def redis_list_basic_examples():
    try:

        print(f"Inside func: redis_list_basic_examples")
        global redisObj
        
        # deleting all tasks from list as queue [FIFO]
        task_queue_key = f"Task_Queue"
        redisObj.delete(task_queue_key)
        
        # adding task in list from left side as queue [FIFO]
        redisObj.lpush(task_queue_key, "Task1")
        redisObj.lpush(task_queue_key, "Task2")
        redisObj.lpush(task_queue_key, "Task3")

        # printing all stored task from list in current order as queue [FIFO]
        # lrange: fetching data using index-range
        print(f"Fetching all stored tasks from list in current order: {redisObj.lrange(task_queue_key, 0, -1)}")
        
        # remove item from right side as queue [FIFO]
        removedTask = redisObj.rpop(task_queue_key)
        print(f"Removed task from redis list from right side: {removedTask}")

        # printing all stored task from list in current order as queue [FIFO]
        # lrange: fetching data using index-range
        print(f"Fetching all stored tasks from list in current order: {redisObj.lrange(task_queue_key, 0, -1)}")


    except Exception as e:
        print(f"Exception occured inside func redis_list_basic_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    redis_list_basic_examples()