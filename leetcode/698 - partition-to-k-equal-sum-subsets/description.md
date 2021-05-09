Given an integer array `` nums `` and an integer `` k ``, return `` true `` if it is possible to divide this array into `` k `` non-empty subsets whose sums are all equal.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [4,3,2,3,5,2,1], k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4], k = 3
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= k &lt;= nums.length &lt;= 16 ``
*   <code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code>