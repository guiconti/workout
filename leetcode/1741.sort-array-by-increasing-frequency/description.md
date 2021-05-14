Given an array of integers `` nums ``, sort the array in __increasing__ order based on the frequency of the values. If multiple values have the same frequency, sort them in __decreasing__ order.

Return the _sorted array_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,1,2,2,2,3]
<strong>Output:</strong> [3,1,1,2,2,2]
<strong>Explanation:</strong> '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,3,1,3,2]
<strong>Output:</strong> [1,3,3,2,2]
<strong>Explanation:</strong> '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [-1,1,-6,4,5,-6,1,4,1]
<strong>Output:</strong> [5,-1,4,4,-6,-6,1,1,1]</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 100 ``
*   `` -100 &lt;= nums[i] &lt;= 100 ``