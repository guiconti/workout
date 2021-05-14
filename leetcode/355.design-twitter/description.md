Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the `` 10 `` most recent tweets in the user's news feed.

Implement the `` Twitter `` class:

*   `` Twitter() `` Initializes your twitter object.
*   `` void postTweet(int userId, int tweetId) `` Composes a new tweet with ID `` tweetId `` by the user `` userId ``. Each call to this function will be made with a unique `` tweetId ``.
*   `` List&lt;Integer&gt; getNewsFeed(int userId) `` Retrieves the `` 10 `` most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be __ordered from most recent to least recent__.
*   `` void follow(int followerId, int followeeId) `` The user with ID `` followerId `` started following the user with ID `` followeeId ``.
*   `` void unfollow(int followerId, int followeeId) `` The user with ID `` followerId `` started unfollowing the user with ID `` followeeId ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
<strong>Output</strong>
[null, null, [5], null, null, [6, 5], null, [5]]

<strong>Explanation</strong>
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -&gt; [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -&gt; [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -&gt; [5], since user 1 is no longer following user 2.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= userId, followerId, followeeId &lt;= 500 ``
*   <code>0 &lt;= tweetId &lt;= 10<sup>4</sup></code>
*   All the tweets have __unique__ IDs.
*   At most <code>3 * 10<sup>4</sup></code> calls will be made to `` postTweet ``, `` getNewsFeed ``, `` follow ``, and `` unfollow ``.