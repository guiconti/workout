Given a binary array `` nums ``, return _the maximum length of a contiguous subarray with an equal number of _`` 0 ``_ and _`` 1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [0,1,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   `` nums[i] `` is either `` 0 `` or `` 1 ``.