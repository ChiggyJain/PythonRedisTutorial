
import redis


def test_redis_connection():
    print(f"Inside func: test_redis_connection\n")
    try:
        redisObj = redis.Redis(host="localhost", port=6379, decode_responses=True)
        pong = redisObj.ping()
        print(f"Redis connected successfully: {pong}\n")
    except Exception as e:
        print(f"Exception occured inside func: test_redis_connection => {e}\n")

if __name__ == "__main__":
    test_redis_connection()