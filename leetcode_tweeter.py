class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.userDict = {}
        self.followDict = {}
        self.news = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.userDict.setdefault(userId, []).append(tweetId)
        self.news.insert(0, tweetId)

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        myid = [userId]
        if userId in self.followDict:
            for i in self.followDict[userId]:
                myid.append(i)

        result = []

        for newId in self.news:
            for i in myid:
                # print(self.userDict)
                # temp = self.userDict.get(i)
                if newId in self.userDict.get(i, []):
                    result.insert(0, newId)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followDict.setdefault(followerId, []).append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        mylist = self.followDict.get(followerId)
        myindex = mylist.index(followeeId)
        self.followDict.get(followerId).pop(myindex)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

twitter = Twitter()
