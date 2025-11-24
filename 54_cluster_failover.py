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

master_nodes = {
    "A" : {"slots" : (0, 5460), "status" : "up"},
    "B" : {"slots" : (5461, 10922), "status" : "up"},
    "C" : {"slots" : (10923, 16383), "status" : "up"}
}

replica_nodes = {
    "A1" : {"master" : "A", "status" : "up"},
    "B1" : {"master" : "B", "status" : "up"},
    "C1" : {"master" : "C", "status" : "up"}
}


def find_master_for_slot(slot):
    for node, data in master_nodes.items():
        start, end = data["slots"]
        if start<=slot<=end and data["status"] == "up":
            return node
    return None

def simulate_failover(failed_master):
    print(f"---- FAILOVER TRIGGERED: Master {failed_master} DOWN ----")
    master_nodes[failed_master]["status"] = "down"
    replica = failed_master + "1"
    new_master_name = replica
    print(f"Promoting Replica {replica} → NEW MASTER")
    master_nodes[new_master_name] = {
        "slots": master_nodes[failed_master]["slots"],
        "status": "up",
    }
    print(f"Cluster updated: {new_master_name} is now Master for slots {master_nodes[new_master_name]['slots']}")



def cluster_failover_demo_examples():
    try:

        print(f"Inside func: cluster_basic_examples")
        global redisObj
        redisObj.flushall()

        key = "user:100"
        slot = compute_slot(key)
        print(f"Key: {key} → Slot: {slot}")
        old_master = find_master_for_slot(slot)
        print(f"Key belongs to Master Node: {old_master}")
        simulate_failover(old_master)
        new_master = find_master_for_slot(slot)
        print(f"After failover: Key routed to NEW Master: {new_master}")
        
    except Exception as e:
        print(f"Exception occured inside func memory_tuning_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    cluster_failover_demo_examples()

