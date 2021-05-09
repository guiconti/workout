You are given two integer arrays `` nums1 `` and `` nums2 `` both of __unique__ elements, where `` nums1 `` is a subset of `` nums2 ``.

Find all the next greater numbers for `` nums1 ``'s elements in the corresponding places of `` nums2 ``.

The Next Greater Number of a number `` x `` in `` nums1 `` is the first greater number to its right in `` nums2 ``. If it does not exist, return `` -1 `` for this number.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums1 = [4,1,2], nums2 = [1,3,4,2]
<strong>Output:</strong> [-1,3,-1]
<strong>Explanation:
</strong>For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums1 = [2,4], nums2 = [1,2,3,4]
<strong>Output:</strong> [3,-1]
<strong>Explanation:</strong>
For number 2 in the first array, the next greater number for it in the second array is 3.
For number 4 in the first array, there is no next greater number for it in the second array, so output -1.</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums1.length &lt;= nums2.length &lt;= 1000 ``
*   <code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>4</sup></code>
*   All integers in `` nums1 `` and `` nums2 `` are __unique__.
*   All the integers of `` nums1 `` also appear in `` nums2 ``.

&nbsp;
__Follow up:__ Could you find an `` O(nums1.length + nums2.length) `` solution?