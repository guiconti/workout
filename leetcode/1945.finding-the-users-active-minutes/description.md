You are given the logs for users' actions on LeetCode, and an integer `` k ``. The logs are represented by a 2D integer array `` logs `` where each <code>logs[i] = [ID<sub>i</sub>, time<sub>i</sub>]</code> indicates that the user with <code>ID<sub>i</sub></code> performed an action at the minute <code>time<sub>i</sub></code>.

__Multiple users__ can perform actions simultaneously, and a single user can perform __multiple actions__ in the same minute.

The __user active minutes (UAM)__ for a given user is defined as the __number of unique minutes__ in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a __1-indexed__ array `` answer `` of size `` k `` such that, for each `` j `` (`` 1 &lt;= j &lt;= k ``), `` answer[j] `` is the __number of users__ whose __UAM__ equals `` j ``.

Return _the array _`` answer ``_ as described above_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
<strong>Output:</strong> [0,2,0,0,0]
<strong>Explanation:</strong>
The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> logs = [[1,1],[2,2],[2,3]], k = 4
<strong>Output:</strong> [1,1,0,0]
<strong>Explanation:</strong>
The user with ID=1 performed a single action at minute 1. Hence, they have a UAM of 1.
The user with ID=2 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
There is one user with a UAM of 1 and one with a UAM of 2.
Hence, answer[1] = 1, answer[2] = 1, and the remaining values are 0.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= logs.length &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= ID<sub>i</sub> &lt;= 10<sup>9</sup></code>
*   <code>1 &lt;= time<sub>i</sub> &lt;= 10<sup>5</sup></code>
*   `` k `` is in the range <code>[The maximum <strong>UAM</strong> for a user, 10<sup>5</sup>]</code>.