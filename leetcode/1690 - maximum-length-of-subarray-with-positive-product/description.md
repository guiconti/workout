Given an array of integers&nbsp;`` nums ``, find&nbsp;the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return&nbsp;_the maximum length of a subarray with positive product_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,-2,-3,4]
<strong>Output:</strong> 4
<strong>Explanation: </strong>The array nums already has a positive product of 24.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [0,1,-2,-3,-4]
<strong>Output:</strong> 3
<strong>Explanation: </strong>The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [-1,-2,-3,0,1]
<strong>Output:</strong> 2
<strong>Explanation: </strong>The longest subarray with positive product is [-1,-2] or [-2,-3].
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [-1,2]
<strong>Output:</strong> 1
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [1,2,3,5,-6,4,0,10]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 10^5 ``
*   `` -10^9 &lt;= nums[i]&nbsp;&lt;= 10^9 ``