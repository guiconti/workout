Given integer array `` nums ``, return _the third maximum number in this array_. If the third maximum does not exist, return the maximum number.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The third maximum is 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The third maximum does not exist, so the maximum (2) is returned instead.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [2,2,3,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>

&nbsp;
__Follow up:__ Can you find an `` O(n) `` solution?