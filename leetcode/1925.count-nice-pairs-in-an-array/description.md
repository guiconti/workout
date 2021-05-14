You are given an array `` nums `` that consists of non-negative integers. Let us define `` rev(x) `` as the reverse of the non-negative integer `` x ``. For example, `` rev(123) = 321 ``, and `` rev(120) = 21 ``. A pair of indices `` (i, j) `` is __nice__ if it satisfies all of the following conditions:

*   `` 0 &lt;= i &lt; j &lt; nums.length ``
*   `` nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) ``

Return _the number of nice pairs of indices_. Since that number can be too large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [42,11,1,97]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [13,10,35,24,76]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code>