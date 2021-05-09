Given an array `` nums `` containing `` n `` distinct numbers in the range `` [0, n] ``, return _the only number in the range that is missing from the array._

__Follow up:__ Could you implement a solution using only `` O(1) `` extra space complexity and `` O(n) `` runtime complexity?

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,0,1]
<strong>Output:</strong> 2
<b>Explanation</b><strong>:</strong> n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<b>Explanation</b><strong>:</strong> n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [9,6,4,2,3,5,7,0,1]
<strong>Output:</strong> 8
<b>Explanation</b><strong>:</strong> n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> 1
<b>Explanation</b><strong>:</strong> n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>
*   `` 0 &lt;= nums[i] &lt;= n ``
*   All the numbers of `` nums `` are __unique__.