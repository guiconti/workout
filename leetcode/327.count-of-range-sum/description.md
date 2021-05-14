Given an integer array `` nums `` and two integers `` lower `` and `` upper ``, return _the number of range sums that lie in_ `` [lower, upper] `` _inclusive_.

Range sum `` S(i, j) `` is defined as the sum of the elements in `` nums `` between indices `` i `` and `` j `` inclusive, where `` i &lt;= j ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [-2,5,-1], lower = -2, upper = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [0], lower = 0, upper = 0
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>
*   <code>-10<sup>5</sup> &lt;= lower &lt;= upper &lt;= 10<sup>5</sup></code>
*   The answer is __guaranteed__ to fit in a __32-bit__ integer.