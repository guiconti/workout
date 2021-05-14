There are `` n `` people, each person has a unique _id_ between `` 0 `` and `` n-1 ``. Given the arrays `` watchedVideos `` and `` friends ``, where `` watchedVideos[i] `` and `` friends[i] `` contain the list of watched videos and the list of friends respectively for the person with `` id = i ``.

Level __1__ of videos are all watched videos by your&nbsp;friends, level __2__ of videos are all watched videos by the friends of your&nbsp;friends and so on. In general, the level `` k `` of videos are all&nbsp;watched videos by people&nbsp;with the shortest path __exactly__ equal&nbsp;to&nbsp;`` k `` with you. Given your&nbsp;`` id `` and the `` level `` of videos, return the list of videos ordered by their frequencies (increasing). For videos with the same frequency order them alphabetically from least to greatest.&nbsp;

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/01/02/leetcode_friends_1.png" style="width: 144px; height: 200px;"/></strong>

<pre>
<strong>Input:</strong> watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
<strong>Output:</strong> ["B","C"] 
<strong>Explanation:</strong> 
You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
Person with id = 1 -&gt; watchedVideos = ["C"]&nbsp;
Person with id = 2 -&gt; watchedVideos = ["B","C"]&nbsp;
The frequencies of watchedVideos by your friends are:&nbsp;
B -&gt; 1&nbsp;
C -&gt; 2
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/01/02/leetcode_friends_2.png" style="width: 144px; height: 200px;"/></strong>

<pre>
<strong>Input:</strong> watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
<strong>Output:</strong> ["D"]
<strong>Explanation:</strong> 
You have id = 0 (green color in the figure) and the only friend of your friends is the person with id = 3 (yellow color in the figure).
</pre>

&nbsp;

__Constraints:__

*   `` n == watchedVideos.length ==&nbsp;friends.length ``
*   `` 2 &lt;= n&nbsp;&lt;= 100 ``
*   `` 1 &lt;=&nbsp;watchedVideos[i].length &lt;= 100 ``
*   `` 1 &lt;=&nbsp;watchedVideos[i][j].length &lt;= 8 ``
*   `` 0 &lt;= friends[i].length &lt; n ``
*   `` 0 &lt;= friends[i][j]&nbsp;&lt; n ``
*   `` 0 &lt;= id &lt; n ``
*   `` 1 &lt;= level &lt; n ``
*   if&nbsp;`` friends[i] `` contains `` j ``, then `` friends[j] `` contains `` i ``