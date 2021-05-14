Given a sorted integer array `` nums `` and an integer `` n ``, add/patch elements to the array such that any number in the range `` [1, n] `` inclusive can be formed by the sum of some elements in the array.

Return _the minimum number of patches required_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,3], n = 6
<strong>Output:</strong> 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,5,10], n = 20
<strong>Output:</strong> 2
Explanation: The two patches can be [2, 4].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,2], n = 5
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 1000 ``
*   <code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   `` nums `` is sorted in __ascending order__.
*   <code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code>