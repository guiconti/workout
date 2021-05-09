You are given an integer array `` nums `` of __even__ length `` n `` and an integer `` limit ``. In one move, you can replace any integer from `` nums `` with another integer between `` 1 `` and `` limit ``, inclusive.

The array `` nums `` is __complementary__ if for all indices `` i `` (__0-indexed__), `` nums[i] + nums[n - 1 - i] `` equals the same number. For example, the array `` [1,2,3,4] `` is complementary because for all indices `` i ``, `` nums[i] + nums[n - 1 - i] = 5 ``.

Return the ___minimum__ number of moves required to make _`` nums ``_ __complementary___.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,4,3], limit = 4
<strong>Output:</strong> 1
<strong>Explanation:</strong> In 1 move, you can change nums to [1,2,<u>2</u>,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,2,1], limit = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> In 2 moves, you can change nums to [<u>2</u>,2,2,<u>2</u>]. You cannot change any number to 3 since 3 &gt; limit.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,1,2], limit = 2
<strong>Output:</strong> 0
<strong>Explanation:</strong> nums is already complementary.
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>2 &lt;= n&nbsp;&lt;=&nbsp;10<sup>5</sup></code>
*   <code>1 &lt;= nums[i]&nbsp;&lt;= limit &lt;=&nbsp;10<sup>5</sup></code>
*   `` n `` is even.