Given an integer array `` nums ``, return _the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,2,3,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [4,2,3,4]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   `` 0 &lt;= nums[i] &lt;= 1000 ``