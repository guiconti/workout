Given an integer array `` nums ``, you need to find one __continuous subarray__ that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return _the shortest such subarray and output its length_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,6,4,8,10,9,15]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code>

&nbsp;
__Follow up:__ Can you solve it in `` O(n) `` time complexity?