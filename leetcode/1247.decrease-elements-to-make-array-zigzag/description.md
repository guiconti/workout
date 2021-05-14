Given an array `` nums `` of integers, a _move_&nbsp;consists of choosing any element and __decreasing it by 1__.

An array `` A `` is a&nbsp;_zigzag array_&nbsp;if either:

*   Every even-indexed element is greater than adjacent elements, ie.&nbsp;`` A[0] &gt; A[1] &lt; A[2] &gt; A[3] &lt; A[4] &gt; ... ``
*   OR, every odd-indexed element is greater than adjacent elements, ie.&nbsp;`` A[0] &lt; A[1] &gt; A[2] &lt; A[3] &gt; A[4] &lt; ... ``

Return the minimum number of moves to transform the given array `` nums `` into a zigzag array.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can decrease 2 to 0 or 3 to 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [9,6,1,6,2]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   `` 1 &lt;= nums[i] &lt;= 1000 ``