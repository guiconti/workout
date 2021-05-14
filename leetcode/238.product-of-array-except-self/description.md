Given an integer array `` nums ``, return _an array_ `` answer `` _such that_ `` answer[i] `` _is equal to the product of all the elements of_ `` nums `` _except_ `` nums[i] ``.

The product of any prefix or suffix of `` nums `` is __guaranteed__ to fit in a __32-bit__ integer.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   `` -30 &lt;= nums[i] &lt;= 30 ``
*   The product of any prefix or suffix of `` nums `` is __guaranteed__ to fit in a __32-bit__ integer.

&nbsp;

__Follow up:__

*   Could you solve it in `` O(n) `` time complexity and without using division?
*   Could you solve it with `` O(1) `` constant space complexity? (The output array __does not__ count as extra space for space complexity analysis.)