
import redis
import time
redisObj = None


def make_redis_connection():
    print(f"Inside func: make_redis_connection\n")
    try:
        global redisObj
        redisObj = redis.Redis(host="localhost", port=6379, decode_responses=True)
        pong = redisObj.ping()
        print(f"Redis connected successfully: {pong}\n")
    except Exception as e:
        print(f"Exception occured inside func: make_redis_connection => {e}\n")



def speed_test_redis_set_operation_method():
    print(f"Inside func: speed_test_redis_set_operation_method\n")
    global redisObj
    satrtTime = time.time()
    for i in range(1, 10001):
        # pass
        redisObj.set(f"test_key_{i}", i)
    endTime = time.time()
    print(f"Time taken for 10,000 set operations: {endTime-satrtTime} seconds\n")

if __name__ == "__main__":
    make_redis_connection()
    speed_test_redis_set_operation_method()