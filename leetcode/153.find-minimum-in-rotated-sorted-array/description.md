Suppose an array of length `` n `` sorted in ascending order is __rotated__ between `` 1 `` and `` n `` times. For example, the array `` nums = [0,1,2,4,5,6,7] `` might become:

*   `` [4,5,6,7,0,1,2] `` if it was rotated `` 4 `` times.
*   `` [0,1,2,4,5,6,7] `` if it was rotated `` 7 `` times.

Notice that __rotating__ an array `` [a[0], a[1], a[2], ..., a[n-1]] `` 1 time results in the array `` [a[n-1], a[0], a[1], a[2], ..., a[n-2]] ``.

Given the sorted rotated array `` nums `` of __unique__ elements, return _the minimum element of this array_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The original array was [1,2,3,4,5] rotated 3 times.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [4,5,6,7,0,1,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [11,13,15,17]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The original array was [11,13,15,17] and it was rotated 4 times. 
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   `` 1 &lt;= n &lt;= 5000 ``
*   `` -5000 &lt;= nums[i] &lt;= 5000 ``
*   All the integers of `` nums `` are __unique__.
*   `` nums `` is sorted and rotated between `` 1 `` and `` n `` times.