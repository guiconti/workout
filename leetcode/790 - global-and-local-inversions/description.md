You are given an integer array `` nums `` of length `` n `` which represents a permutation of all the integers in the range `` [0, n - 1] ``.

The number of __global inversions__ is the number of the different pairs `` (i, j) `` where:

*   `` 0 &lt;= i &lt; j &lt; n ``
*   `` nums[i] &gt; nums[j] ``

The number of __local inversions__ is the number of indices `` i `` where:

*   `` 0 &lt;= i &lt; n - 1 ``
*   `` nums[i] &gt; nums[i + 1] ``

Return `` true `` _if the number of __global inversions__ is equal to the number of __local inversions___.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,0,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> There is 1 global inversion and 1 local inversion.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are 2 global inversions and 1 local inversion.
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   `` 0 &lt;= nums[i] &lt; n ``
*   All the integers of `` nums `` are __unique__.
*   `` nums `` is a permutation of all the numbers in the range `` [0, n - 1] ``.