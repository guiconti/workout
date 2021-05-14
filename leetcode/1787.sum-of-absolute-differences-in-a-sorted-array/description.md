You are given an integer array `` nums `` sorted in __non-decreasing__ order.

Build and return _an integer array _`` result ``_ with the same length as _`` nums ``_ such that _`` result[i] ``_ is equal to the __summation of absolute differences__ between _`` nums[i] ``_ and all the other elements in the array._

In other words, `` result[i] `` is equal to `` sum(|nums[i]-nums[j]|) `` where `` 0 &lt;= j &lt; nums.length `` and `` j != i `` (__0-indexed__).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,3,5]
<strong>Output:</strong> [4,3,5]
<strong>Explanation:</strong> Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,4,6,8,10]
<strong>Output:</strong> [24,15,13,15,21]
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= nums[i + 1] &lt;= 10<sup>4</sup></code>