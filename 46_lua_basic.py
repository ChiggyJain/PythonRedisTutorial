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


def lua_basic_examples():
    try:

        print(f"Inside func: lua_basic_examples")
        global redisObj

        keyName = "Counter"
        redisObj.delete(keyName)
        redisObj.set(keyName, 101)

        luaScript = """
            local val = redis.call('GET', KEYS[1])
            val = tonumber(val) + 9
            redis.call('SET', KEYS[1], val)
            return val
        """
        result = redisObj.eval(luaScript, 1, keyName)
        print(f"Lua Result: {result}")
        print(f"Rddis in Key-Name: {keyName}, Val: {redisObj.get(keyName)}")

        

    except Exception as e:
        print(f"Exception occured inside func lua_basic_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    lua_basic_examples()

