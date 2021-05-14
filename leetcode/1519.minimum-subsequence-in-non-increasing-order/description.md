Given the array `` nums ``, obtain a subsequence of the array whose sum of elements is __strictly greater__ than the sum of the non&nbsp;included elements in such subsequence.&nbsp;

If there are multiple solutions, return the subsequence with __minimum size__ and if there still exist multiple solutions, return the subsequence with the __maximum total sum__ of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.&nbsp;

Note that the solution with the given constraints is guaranteed to be&nbsp;__unique__. Also return the answer sorted in __non-increasing__ order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [4,3,10,9,8]
<strong>Output:</strong> [10,9] 
<strong>Explanation:</strong> The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included, however, the subsequence [10,9] has the maximum total sum of its elements.&nbsp;
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [4,4,7,6,7]
<strong>Output:</strong> [7,7,6] 
<strong>Explanation:</strong> The subsequence [7,7] has the sum of its elements equal to 14 which is not strictly greater than the sum of elements not included (14 = 4 + 4 + 6). Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions. Note the subsequence has to returned in non-decreasing order.  
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [6]
<strong>Output:</strong> [6]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 500 ``
*   `` 1 &lt;= nums[i] &lt;= 100 ``