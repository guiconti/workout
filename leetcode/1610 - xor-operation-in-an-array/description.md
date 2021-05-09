Given an integer `` n `` and an integer `` start ``.

Define an array `` nums `` where `` nums[i] = start + 2*i `` (0-indexed) and `` n == nums.length ``.

Return the bitwise&nbsp;XOR&nbsp;of all elements of `` nums ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 5, start = 0
<strong>Output:</strong> 8
<strong>Explanation: </strong>Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 4, start = 3
<strong>Output:</strong> 8
<strong>Explanation: </strong>Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 1, start = 7
<strong>Output:</strong> 7
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 10, start = 5
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 1000 ``
*   `` 0 &lt;= start &lt;= 1000 ``
*   `` n == nums.length ``