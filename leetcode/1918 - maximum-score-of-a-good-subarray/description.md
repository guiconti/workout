You are given an array of integers `` nums `` __(0-indexed)__ and an integer `` k ``.

The __score__ of a subarray `` (i, j) `` is defined as `` min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) ``. A __good__ subarray is a subarray where `` i &lt;= k &lt;= j ``.

Return _the maximum possible __score__ of a __good__ subarray._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,4,3,7,4,5], k = 3
<strong>Output:</strong> 15
<strong>Explanation:</strong> The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [5,5,4,5,4,1,1,1], k = 0
<strong>Output:</strong> 20
<strong>Explanation:</strong> The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 2 * 10<sup>4</sup></code>
*   `` 0 &lt;= k &lt; nums.length ``