You are given an integer array `` nums `` and an integer `` goal ``.

You want to choose a subsequence of `` nums `` such that the sum of its elements is the closest possible to `` goal ``. That is, if the sum of the subsequence's elements is `` sum ``, then you want to __minimize the absolute difference__ `` abs(sum - goal) ``.

Return _the __minimum__ possible value of_ `` abs(sum - goal) ``.

Note that a subsequence of an array is an array formed by removing some elements __(possibly all or none)__ of the original array.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [5,-7,3,5], goal = 6
<strong>Output:</strong> 0
<strong>Explanation:</strong> Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [7,-9,15,-2], goal = -5
<strong>Output:</strong> 1
<strong>Explanation:</strong> Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,3], goal = -7
<strong>Output:</strong> 7
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 40 ``
*   <code>-10<sup>7</sup> &lt;= nums[i] &lt;= 10<sup>7</sup></code>
*   <code>-10<sup>9</sup> &lt;= goal &lt;= 10<sup>9</sup></code>