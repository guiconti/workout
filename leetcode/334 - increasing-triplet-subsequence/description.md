Given an integer array `` nums ``, return `` true ``_ if there exists a triple of indices _`` (i, j, k) ``_ such that _`` i &lt; j &lt; k ``_ and _`` nums[i] &lt; nums[j] &lt; nums[k] ``. If no such indices exists, return `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> Any triplet where i &lt; j &lt; k is valid.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [5,4,3,2,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> No triplet exists.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [2,1,5,0,4,6]
<strong>Output:</strong> true
<strong>Explanation:</strong> The triplet (3, 4, 5) is valid because nums[3] == 0 &lt; nums[4] == 4 &lt; nums[5] == 6.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>

&nbsp;
__Follow up:__ Could you implement a solution that runs in `` O(n) `` time complexity and `` O(1) `` space complexity?