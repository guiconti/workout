There is a function `` signFunc(x) `` that returns:

*   `` 1 `` if `` x `` is positive.
*   `` -1 `` if `` x `` is negative.
*   `` 0 `` if `` x `` is equal to `` 0 ``.

You are given an integer array `` nums ``. Let `` product `` be the product of all values in the array `` nums ``.

Return `` signFunc(product) ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [-1,-2,-3,-4,3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The product of all values in the array is 144, and signFunc(144) = 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,5,0,2,-3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The product of all values in the array is 0, and signFunc(0) = 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [-1,1,-1,1,-1]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The product of all values in the array is -1, and signFunc(-1) = -1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   `` -100 &lt;= nums[i] &lt;= 100 ``