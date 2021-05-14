Given an array `` nums ``&nbsp;of positive integers, return the longest possible length of an array prefix of `` nums ``, such that it is possible to remove __exactly one__ element from this prefix so that every number that has appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,2,1,1,5,3,3,5]
<strong>Output:</strong> 7
<strong>Explanation:</strong> For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4]=5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
<strong>Output:</strong> 13
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,1,1,2,2,2]
<strong>Output:</strong> 5
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [10,2,8,9,3,8,1,5,2,3,7,6]
<strong>Output:</strong> 8
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= nums.length &lt;= 10^5 ``
*   `` 1 &lt;= nums[i] &lt;= 10^5 ``