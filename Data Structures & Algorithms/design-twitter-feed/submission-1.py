class Twitter:

    def __init__(self):
        self.time = 0
        self.user2tweets = defaultdict(deque)
        self.user2follow = defaultdict(set)



    def postTweet(self, userId: int, tweetId: int) -> None:
        cur_list = self.user2tweets[userId]
        cur_list.append((self.time, tweetId))
        if len(cur_list) > 10:
            cur_list.popleft()
        self.time += 1
        return 

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = [] # maxheap
        user_list = list(self.user2follow[userId]) + [userId]
        for user in user_list:
            for time, tweet in self.user2tweets[user]:
                heapq.heappush(pq, (-time, tweet))
        res = []
        while pq and len(res) < 10:
            _, tweet_id = heapq.heappop(pq)
            res.append(tweet_id)
        return res
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.user2follow[followerId].add(followeeId)
        return 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.user2follow[followerId].discard(followeeId)
        return
