Given an integer array `` nums ``, find a contiguous non-empty subarray within the array that has the largest product, and return _the product_.

It is __guaranteed__ that the answer will fit in a __32-bit__ integer.

A __subarray__ is a contiguous subsequence of the array.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,3,-2,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [2,3] has the largest product 6.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-2,0,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The result cannot be 2, because [-2,-1] is not a subarray.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code>
*   `` -10 &lt;= nums[i] &lt;= 10 ``
*   The product of any prefix or suffix of `` nums `` is __guaranteed__ to fit in a __32-bit__ integer.