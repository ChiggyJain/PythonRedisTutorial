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


def memory_tuning_examples():
    try:

        print(f"Inside func: memory_tuning_examples")
        global redisObj
        redisObj.flushall()

        print(f"--Memory Usage Demo--")
        redisObj.set("Demo:String", "Hello World")
        print("Memory usage of Demo:String:", redisObj.memory_usage("Demo:String"), "bytes")

        # creating large list
        redisObj.delete("Demo-List")
        for i in range(10001):
            redisObj.lpush("Demo-List", "X" * 50)
        print("Memory usage of Demo-List:", redisObj.memory_usage("Demo-List"), "bytes")

        print(f"---- MEMORY STATS ----")
        stats = redisObj.memory_stats()
        print("Allocator:", stats.get("jemalloc.allocated"))
        print("Fragmentation ratio:", stats.get("fragmentation"))
        print("RSS memory:", stats.get("rss"))

        print(f"--- INFO MEMORY ----")
        mem = redisObj.info("memory")
        print("Used Memory:", mem["used_memory_human"])
        print("Peak Memory:", mem["used_memory_peak_human"])
        print("Fragmentation Ratio:", mem["mem_fragmentation_ratio"])

        print(f"---- OBJECT ENCODING ----")
        print("Encoding of Demo-String:", redisObj.object("encoding", "Demo-String"))
        print("Encoding of Demo-List:", redisObj.object("encoding", "Demo-List"))

        print(f"---- MEMORY PURGE (Defragmentation) ----")
        redisObj.execute_command("MEMORY PURGE")
        print("Purge triggered. Check memory again after few seconds.")
        time.sleep(2)
        mem2 = redisObj.info("memory")
        print("Fragmentation After Purge:", mem2["mem_fragmentation_ratio"])

    except Exception as e:
        print(f"Exception occured inside func memory_tuning_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    memory_tuning_examples()

