You are given an integer array, `` nums ``, and an integer `` k ``. `` nums `` comprises of only `` 0 ``'s and `` 1 ``'s. In one move, you can choose two __adjacent__ indices and swap their values.

Return _the __minimum__ number of moves required so that _`` nums ``_ has _`` k ``_ __consecutive__ _`` 1 ``_'s_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,0,0,1,0,1], k = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> In 1 move, nums could be [1,0,0,0,<u>1</u>,<u>1</u>] and have 2 consecutive 1's.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,0,0,0,0,0,1,1], k = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,<u>1</u>,<u>1</u>,<u>1</u>].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,1,0,1], k = 2
<strong>Output:</strong> 0
<strong>Explanation:</strong> nums already has 2 consecutive 1's.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   `` nums[i] `` is `` 0 `` or `` 1 ``.
*   `` 1 &lt;= k &lt;= sum(nums) ``