You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are __arranged in a circle.__ That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and&nbsp;__it will automatically contact the police if two adjacent houses were broken into on the same night__.

Given an integer array `` nums `` representing the amount of money of each house, return _the maximum amount of money you can rob tonight __without alerting the police___.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 100 ``
*   `` 0 &lt;= nums[i] &lt;= 1000 ``