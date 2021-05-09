Given an integer array `` nums ``, reorder it such that `` nums[0] &lt; nums[1] &gt; nums[2] &lt; nums[3]... ``.

You may assume the input array always has a valid answer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,5,1,1,6,4]
<strong>Output:</strong> [1,6,1,5,1,4]
<strong>Explanation:</strong> [1,4,1,5,1,6] is also accepted.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,3,2,2,3,1]
<strong>Output:</strong> [2,3,1,3,1,2]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code>
*   `` 0 &lt;= nums[i] &lt;= 5000 ``
*   It is guaranteed that there will be an answer for the given input `` nums ``.

&nbsp;
__Follow Up:__ Can you do it in `` O(n) `` time and/or __in-place__ with `` O(1) `` extra space?