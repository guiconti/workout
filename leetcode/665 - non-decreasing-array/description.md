Given an array `` nums `` with `` n `` integers, your task is to check if it could become non-decreasing by modifying __at most one element__.

We define an array is non-decreasing if `` nums[i] &lt;= nums[i + 1] `` holds for every `` i `` (__0-based__) such that (`` 0 &lt;= i &lt;= n - 2 ``).

&nbsp;

__Example 1:__

<strong>Input:</strong> nums = [4,2,3]
    <strong>Output:</strong> true
    <strong>Explanation:</strong> You could modify the first 4 to <code>1</code> to get a non-decreasing array.

__Example 2:__

<pre>
<strong>Input:</strong> nums = [4,2,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> You can't get a non-decreasing array by modify at most one element.
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code>