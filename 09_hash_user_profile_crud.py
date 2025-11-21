
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


class UserProfile:

    @staticmethod
    def createUserProfileDetails(userId, userInfoObj):
        hashKey = f"User-ID:{userId}"
        return redisObj.hset(hashKey, mapping=userInfoObj)

    @staticmethod
    def getUserProfileDetails(userId):
        hashKey = f"User-ID:{userId}"
        return redisObj.hgetall(hashKey)
        
    @staticmethod
    def getUserProfileSingleRespectiveFieldDetails(userId, fieldName):
        hashKey = f"User-ID:{userId}"
        return redisObj.hget(hashKey, fieldName)
    
    @staticmethod
    def updateUserProfileSingleRespectiveFieldDetails(userId, fieldName, fieldValue):
        hashKey = f"User-ID:{userId}"
        return redisObj.hset(hashKey, fieldName, fieldValue)

    @staticmethod
    def deleteUserProfileDetails(userId):
        hashKey = f"User-ID:{userId}"
        return redisObj.delete(hashKey)


def redis_hash_userprofile_crud_operations_examples():
    try:

        print(f"Inside func: redis_hash_userprofile_crud_operations_examples")
        global redisObj
        
        userId = "113"
        hashKey = f"User-ID:{userId}"
        redisObj.delete(hashKey)
        
        userProfileInfo = {
            "userId" : userId,
            "userFullName" : "Chirag D Jain",
            "userMobile" : "9975967186",
            "userEmail" : "cjain9975@gmail.com",
            "userRole" : "Developer"
        }

        ## creating user profile
        print(f"User profile is created: {UserProfile.createUserProfileDetails(userId, userProfileInfo)}")
        print(f"Fetching User profile all details: {UserProfile.getUserProfileDetails(userId)}")
        print(f"Fetching User profile mobile field details: {UserProfile.getUserProfileSingleRespectiveFieldDetails(userId, "userMobile")}")
        print(f"Fetching User profile address field details: {UserProfile.getUserProfileSingleRespectiveFieldDetails(userId, "userAddress")}")
        print(f"Updating User profile mobile field details: {UserProfile.updateUserProfileSingleRespectiveFieldDetails(userId, "userMobile", "111")}")
        print(f"Fetching User profile all details: {UserProfile.getUserProfileDetails(userId)}")


    except Exception as e:
        print(f"Exception occured inside func redis_hash_userprofile_crud_operations_examples: {e}")
    

if __name__ == "__main__":
    make_redis_connection()
    redis_hash_userprofile_crud_operations_examples()