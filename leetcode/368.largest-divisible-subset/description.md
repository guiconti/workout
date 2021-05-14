Given a set of __distinct__ positive integers `` nums ``, return the largest subset `` answer `` such that every pair `` (answer[i], answer[j]) `` of elements in this subset satisfies:

*   `` answer[i] % answer[j] == 0 ``, or
*   `` answer[j] % answer[i] == 0 ``

If there are multiple solutions, return any of them.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> [1,3] is also accepted.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,4,8]
<strong>Output:</strong> [1,2,4,8]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   <code>1 &lt;= nums[i] &lt;= 2 * 10<sup>9</sup></code>
*   All the integers in `` nums `` are __unique__.