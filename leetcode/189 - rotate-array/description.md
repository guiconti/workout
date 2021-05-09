Given an array, rotate the array to the right by `` k `` steps, where `` k `` is non-negative.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5,6,7], k = 3
<strong>Output:</strong> [5,6,7,1,2,3,4]
<strong>Explanation:</strong>
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-1,-100,3,99], k = 2
<strong>Output:</strong> [3,99,-1,-100]
<strong>Explanation:</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>
*   <code>0 &lt;= k &lt;= 10<sup>5</sup></code>

&nbsp;

__Follow up:__

*   Try to come up with as many solutions as you can. There are at least __three__ different ways to solve this problem.
*   Could you do it in-place with `` O(1) `` extra space?