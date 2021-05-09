Given an integer array nums, return all the triplets `` [nums[i], nums[j], nums[k]] `` such that `` i != j ``, `` i != k ``, and `` j != k ``, and `` nums[i] + nums[j] + nums[k] == 0 ``.

Notice that the solution set must not contain duplicate triplets.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = []
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= nums.length &lt;= 3000 ``
*   <code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code>