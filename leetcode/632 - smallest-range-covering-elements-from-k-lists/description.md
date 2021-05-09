You have `` k `` lists of sorted integers in __non-decreasing&nbsp;order__. Find the __smallest__ range that includes at least one number from each of the `` k `` lists.

We define the range `` [a, b] `` is smaller than range `` [c, d] `` if `` b - a &lt; d - c `` __or__ `` a &lt; c `` if `` b - a == d - c ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
<strong>Output:</strong> [20,24]
<strong>Explanation: </strong>
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [[1,2,3],[1,2,3],[1,2,3]]
<strong>Output:</strong> [1,1]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [[10,10],[11,11]]
<strong>Output:</strong> [10,11]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [[10],[11]]
<strong>Output:</strong> [10,11]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [[1],[2],[3],[4],[5],[6],[7]]
<strong>Output:</strong> [1,7]
</pre>

&nbsp;

__Constraints:__

*   `` nums.length == k ``
*   `` 1 &lt;= k &lt;= 3500 ``
*   `` 1 &lt;= nums[i].length &lt;= 50 ``
*   <code>-10<sup>5</sup> &lt;= nums[i][j] &lt;= 10<sup>5</sup></code>
*   `` nums[i] ``&nbsp;is sorted in __non-decreasing__ order.