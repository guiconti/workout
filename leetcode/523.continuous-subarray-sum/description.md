Given an integer array `` nums `` and an integer `` k ``, return `` true `` _if _`` nums ``_ has a continuous subarray of size __at least two__ whose elements sum up to a multiple of_ `` k ``_, or _`` false ``_ otherwise_.

An integer `` x `` is a multiple of `` k `` if there exists an integer `` n `` such that `` x = n * k ``. `` 0 `` is __always__ a multiple of `` k ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [23,<u>2,4</u>,6,7], k = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [<u>23,2,6,4,7</u>], k = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [23,2,6,4,7], k = 13
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code>
*   <code>0 &lt;= sum(nums[i]) &lt;= 2<sup>31</sup> - 1</code>
*   <code>1 &lt;= k &lt;= 2<sup>31</sup> - 1</code>