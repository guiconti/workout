Given an integer array `` nums `` sorted in __non-decreasing__ order, return _an array of __the squares of each number__ sorted in non-decreasing order_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [-4,-1,0,3,10]
<strong>Output:</strong> [0,1,9,16,100]
<strong>Explanation:</strong> After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-7,-3,2,3,11]
<strong>Output:</strong> [4,9,9,49,121]
</pre>

&nbsp;

__Constraints:__

*   <code><span>1 &lt;= nums.length &lt;= </span>10<sup>4</sup></code>
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   `` nums `` is sorted in __non-decreasing__ order.

&nbsp;
__Follow up:__ Squaring each element and sorting the new array is very trivial, could you find an `` O(n) `` solution using a different approach?