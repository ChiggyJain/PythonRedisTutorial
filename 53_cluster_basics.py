import redis
import time
import binascii
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


def compute_slot(key: str) -> int:
    # Cluster uses CRC16(key) % 16384
    crc = binascii.crc_hqx(key.encode(), 0)
    return crc % 16384

def cluster_basic_examples():
    try:

        print(f"Inside func: cluster_basic_examples")
        global redisObj
        redisObj.flushall()

        keys = ["user:1", "order:55", "cart:999", "session:abc", "profile:chirag"]
        for k in keys:
            slot = compute_slot(k)
            print(f"Key: {k.ljust(15)} → Slot: {slot}")
        
        print(f"---- Simulating 3-node cluster ----")
        print("Slots 0-5460    → Node A")
        print("Slots 5461-10922 → Node B")
        print("Slots 10923-16383 → Node C")
        for k in keys:
            slot = compute_slot(k)
            if slot <= 5460:
                node = "Node A"
            elif slot <= 10922:
                node = "Node B"
            else:
                node = "Node C"
            print(f"Key {k} → Slot {slot} → {node}")

        
    except Exception as e:
        print(f"Exception occured inside func memory_tuning_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    cluster_basic_examples()

