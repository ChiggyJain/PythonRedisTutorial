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


def lua_advanced_examples():
    try:

        print(f"Inside func: lua_advanced_examples")
        global redisObj

        keyName = "Initial-Stock"
        redisObj.delete(keyName)
        redisObj.set(keyName, 3)

        luaScript = """
            local stock = tonumber(redis.call('GET', KEYS[1]))
            if stock > 0 then
                redis.call('DECR', KEYS[1])
                return stock -1 
            else
                return -1
            end    
        """
        print(f"Initital stock in Key-Name: {keyName}, Val: {redisObj.get(keyName)}")
        script = redisObj.register_script(luaScript)
        print(f"Purchase-Item-Attempt-1: {script(keys=[keyName], args=[])}")
        print(f"Purchase-Item-Attempt-2: {script(keys=[keyName], args=[])}")
        print(f"Purchase-Item-Attempt-3: {script(keys=[keyName], args=[])}")
        print(f"Purchase-Item-Attempt-4: {script(keys=[keyName], args=[])}")
        print(f"Purchase-Item-Attempt-5: {script(keys=[keyName], args=[])}")
        print(f"Final stock in Key-Name: {keyName}, Val: {redisObj.get(keyName)}")

        

    except Exception as e:
        print(f"Exception occured inside func lua_advanced_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    lua_advanced_examples()

