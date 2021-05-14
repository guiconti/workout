There is an integer array `` nums `` sorted in non-decreasing order (not necessarily with __distinct__ values).

Before being passed to your function, `` nums `` is __rotated__ at an unknown pivot index `` k `` (`` 0 &lt;= k &lt; nums.length ``) such that the resulting array is `` [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] `` (__0-indexed__). For example, `` [0,1,2,4,4,4,5,6,6,7] `` might be rotated at pivot index `` 5 `` and become `` [4,5,6,6,7,0,1,2,4,4] ``.

Given the array `` nums `` __after__ the rotation and an integer `` target ``, return `` true ``_ if _`` target ``_ is in _`` nums ``_, or _`` false ``_ if it is not in _`` nums ``_._

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [2,5,6,0,0,1,2], target = 0
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [2,5,6,0,0,1,2], target = 3
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 5000 ``
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   `` nums `` is guaranteed to be rotated at some pivot.
*   <code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code>

&nbsp;
__Follow up:__ This problem is the same as <a href="/problems/search-in-rotated-sorted-array/description/" target="_blank">Search in Rotated Sorted Array</a>, where `` nums `` may contain __duplicates__. Would this affect the runtime complexity? How and why?