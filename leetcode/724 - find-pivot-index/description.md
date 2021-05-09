Given an array of integers `` nums ``, calculate the __pivot index__ of this array.

The __pivot index__ is the index where the sum of all the numbers __strictly__ to the left of the index is equal to the sum of all the numbers __strictly__ to the index's right.

If the index is on the left edge of the array, then the left sum is `` 0 `` because there are no elements to the left. This also applies to the right edge of the array.

Return _the __leftmost pivot index___. If no such index exists, return -1.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,7,3,6,5,6]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
There is no index that satisfies the conditions in the problem statement.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [2,1,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   `` -1000 &lt;= nums[i] &lt;= 1000 ``