Given an array of integers `` nums ``, half of the integers in `` nums `` are __odd__, and the other half are __even__.

Sort the array so that whenever `` nums[i] `` is odd, `` i `` is __odd__, and whenever `` nums[i] `` is even, `` i `` is __even__.

Return _any answer array that satisfies this condition_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [4,2,5,7]
<strong>Output:</strong> [4,5,2,7]
<strong>Explanation:</strong> [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,3]
<strong>Output:</strong> [2,3]
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code>
*   `` nums.length `` is even.
*   Half of the integers in `` nums `` are even.
*   `` 0 &lt;= nums[i] &lt;= 1000 ``

&nbsp;

__Follow Up:__ Could you solve it in-place?