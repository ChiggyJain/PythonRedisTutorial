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


def eviction_policy_examples():
    try:

        print(f"Inside func: eviction_policy_examples")
        global redisObj
        redisObj.flushall()

        print(f"---Current Eviction Policy---")
        infoObj = redisObj.info("memory")
        print(f"Info-Objects: {infoObj}")
        print(f"Max-Memory: {infoObj.get('maxmemory')}")
        print(f"Memory-Eviction-Policy: {redisObj.config_get("maxmemory-policy")}")
        print(f"---- Setting policy to allkeys-lru for demo ----")
        redisObj.config_set("maxmemory-policy", "allkeys-lru")
        print(f"Memory-Eviction-Policy: {redisObj.config_get("maxmemory-policy")}")
        print(f"Setting max-memory as 1MB")
        redisObj.config_set("maxmemory", "0")
        print(f"--- Inserting many keys ----")
        for i in range(1, 11):
            if i % 5000 == 0:
                redisObj.set(f"LRU-Test:{i}", "x" * 1000)
                print(f"Inserted {i} keys")
                mem = redisObj.info("memory")["used_memory_human"]
                print("Memory used:", mem)
                time.sleep(0.2)
        print(f"---- Checking eviction stats ----")
        stats = redisObj.info("stats")
        print("Evicted keys:", stats.get("evicted_keys"))


        redisObj.set(f"LRU-Test:1", "x" * 1000)
        print(f"Memory usage by this specific key (LRU-Test:1):{redisObj.memory_usage("LRU-Test:1")}")
        print(f"Memory stats: {redisObj.memory_stats()}")
        print(f"Purge Memory: {redisObj.execute_command("MEMORY PURGE")}")
        print(f"Object encoding optimization by specific key: {redisObj.object("encoding", "LRU-Test:1")}")


    except Exception as e:
        print(f"Exception occured inside func eviction_policy_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    eviction_policy_examples()

