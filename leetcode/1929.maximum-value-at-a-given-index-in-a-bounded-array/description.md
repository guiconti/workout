You are given three positive integers:&nbsp;`` n ``, `` index ``, and `` maxSum ``. You want to construct an array `` nums `` (__0-indexed__)__ __that satisfies the following conditions:

*   `` nums.length == n ``
*   `` nums[i] `` is a __positive__ integer where `` 0 &lt;= i &lt; n ``.
*   `` abs(nums[i] - nums[i+1]) &lt;= 1 `` where `` 0 &lt;= i &lt; n-1 ``.
*   The sum of all the elements of `` nums `` does not exceed `` maxSum ``.
*   `` nums[index] `` is __maximized__.

Return `` nums[index] ``_ of the constructed array_.

Note that `` abs(x) `` equals `` x `` if `` x &gt;= 0 ``, and `` -x `` otherwise.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 4, index = 2,  maxSum = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> nums = [1,2,<u><strong>2</strong></u>,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 6, index = 1,  maxSum = 10
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= maxSum &lt;= 10<sup>9</sup></code>
*   `` 0 &lt;= index &lt; n ``