Given the array `` nums `` consisting of `` n `` positive integers. You computed the sum of all non-empty continous subarrays from&nbsp;the array and then sort them in non-decreasing order, creating a new array of `` n * (n + 1) / 2 ``&nbsp;numbers.

_Return the sum of the numbers from index _`` left ``_ to index _`` right `` (__indexed from 1__)_, inclusive, in the&nbsp;new array.&nbsp;_Since the answer can be a huge number return it modulo 10^9 + 7.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4], n = 4, left = 1, right = 5
<strong>Output:</strong> 13 
<strong>Explanation:</strong> All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4], n = 4, left = 3, right = 4
<strong>Output:</strong> 6
<strong>Explanation:</strong> The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4], n = 4, left = 1, right = 10
<strong>Output:</strong> 50
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 10^3 ``
*   `` nums.length == n ``
*   `` 1 &lt;= nums[i] &lt;= 100 ``
*   `` 1 &lt;= left &lt;= right&nbsp;&lt;= n * (n + 1) / 2 ``