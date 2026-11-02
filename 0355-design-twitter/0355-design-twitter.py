class Twitter:

    def __init__(self):
        self.tweets = {}
        self.time = 0
        self.following = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        #one userid multiple tweetid
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
       
    def getNewsFeed(self, userId: int) -> list[int]:
        #return tweetid by using userid

        users = {userId}
        if userId in self.following:
            users.update(self.following[userId])

        import heapq
        heap = []
        
        for u in users:
            if u in self.tweets:
                for time, newsid in self.tweets[u]:
                    heapq.heappush(heap, (time, newsid))
                    
                    if len(heap) > 10:
                        heapq.heappop(heap)

        res = []
        while heap:
            _, newsid = heapq.heappop(heap)
            res.append(newsid)

        return res[::-1]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        #one userid multiple followeeid

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)