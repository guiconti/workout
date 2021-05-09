You are given an integer array `` nums `` and an integer `` target ``.

You want to build an __expression__ out of nums by adding one of the symbols `` '+' `` and `` '-' `` before each integer in nums and then concatenate all the integers.

*   For example, if `` nums = [2, 1] ``, you can add a `` '+' `` before `` 2 `` and a `` '-' `` before `` 1 `` and concatenate them to build the expression `` "+2-1" ``.

Return the number of different __expressions__ that you can build, which evaluates to `` target ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1], target = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1], target = 1
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 20 ``
*   `` 0 &lt;= nums[i] &lt;= 1000 ``
*   `` 0 &lt;= sum(nums[i]) &lt;= 1000 ``
*   `` -1000 &lt;= target &lt;= 1000 ``