from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 1
        self.userposts = defaultdict(list)
        self.followee = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userposts[userId].append((-self.time, tweetId))
        self.time +=1

    def getNewsFeed(self, userId: int) -> List[int]:
        users=set([userId])
        followers = self.followee[userId]
        users.update(followers)

        tweets = []
        for user in users:
            tweets.extend(self.userposts[user])
        
        heapq.heapify(tweets)

        results = []
        while tweets and len(results)< 10:
            results.append(heapq.heappop(tweets)[1])

        return results 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].discard(followeeId)
        

