Given an array `` nums `` and an integer <code><font face="monospace">target</font></code>.

Return the maximum number of __non-empty__&nbsp;__non-overlapping__ subarrays such that the sum of values in each subarray is equal to <code><font face="monospace">target</font></code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1], target = 2
<strong>Output:</strong> 2
<strong>Explanation: </strong>There are 2 non-overlapping subarrays [<strong>1,1</strong>,1,<strong>1,1</strong>] with sum equals to target(2).
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-1,3,5,1,4,2,-9], target = 6
<strong>Output:</strong> 2
<strong>Explanation: </strong>There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [-2,6,6,3,5,4,1,2,8], target = 10
<strong>Output:</strong> 3
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [0,0,0], target = 0
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;=&nbsp;10^5 ``
*   `` -10^4 &lt;= nums[i] &lt;=&nbsp;10^4 ``
*   `` 0 &lt;= target &lt;= 10^6 ``