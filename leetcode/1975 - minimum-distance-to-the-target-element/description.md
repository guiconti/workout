Given an integer array `` nums `` __(0-indexed)__ and two integers `` target `` and `` start ``, find an index `` i `` such that `` nums[i] == target `` and `` abs(i - start) `` is __minimized__. Note that&nbsp;`` abs(x) ``&nbsp;is the absolute value of `` x ``.

Return `` abs(i - start) ``.

It is __guaranteed__ that `` target `` exists in `` nums ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5], target = 5, start = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1], target = 1, start = 0
<strong>Output:</strong> 0
<strong>Explanation:</strong> nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
<strong>Output:</strong> 0
<strong>Explanation:</strong> Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   <code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   `` 0 &lt;= start &lt; nums.length ``
*   `` target `` is in `` nums ``.