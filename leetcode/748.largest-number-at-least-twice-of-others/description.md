You are given an integer array `` nums `` where the largest integer is __unique__.

Determine whether the largest element in the array is __at least twice__ as much as every other number in the array. If it is, return _the __index__ of the largest element, or return _`` -1 ``_ otherwise_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,6,1,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 4 is less than twice the value of 3, so we return -1.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> 1 is trivially at least twice the value as any other number because there are no other numbers.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 50 ``
*   `` 0 &lt;= nums[i] &lt;= 100 ``
*   The largest element in `` nums `` is unique.