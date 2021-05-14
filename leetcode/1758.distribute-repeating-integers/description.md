You are given an array of `` n `` integers, `` nums ``, where there are at most `` 50 `` unique values in the array. You are also given an array of `` m `` customer order quantities, `` quantity ``, where `` quantity[i] `` is the amount of integers the <code>i<sup>th</sup></code> customer ordered. Determine if it is possible to distribute `` nums `` such that:

*   The <code>i<sup>th</sup></code> customer gets __exactly__ `` quantity[i] `` integers,
*   The integers the <code>i<sup>th</sup></code> customer gets are __all equal__, and
*   Every customer is satisfied.

Return `` true ``_ if it is possible to distribute _`` nums ``_ according to the above conditions_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4], quantity = [2]
<strong>Output:</strong> false
<strong>Explanation:</strong> The 0th customer cannot be given two different integers.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,3], quantity = [2]
<strong>Output:</strong> true
<strong>Explanation:</strong> The 0th customer is given [3,3]. The integers [1,2] are not used.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,1,2,2], quantity = [2,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> The 0th customer is given [1,1], and the 1st customer is given [2,2].
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [1,1,2,3], quantity = [2,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> Although the 0th customer could be given [1,1], the 1st customer cannot be satisfied.</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1], quantity = [2,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> The 0th customer is given [1,1], and the 1st customer is given [1,1,1].
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   `` 1 &lt;= nums[i] &lt;= 1000 ``
*   `` m == quantity.length ``
*   `` 1 &lt;= m &lt;= 10 ``
*   <code>1 &lt;= quantity[i] &lt;= 10<sup>5</sup></code>
*   There are at most `` 50 `` unique values in `` nums ``.