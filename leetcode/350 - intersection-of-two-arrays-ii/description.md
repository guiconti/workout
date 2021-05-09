Given two integer arrays `` nums1 `` and `` nums2 ``, return _an array of their intersection_. Each element in the result must appear as many times as it shows in both arrays and you may return the result in __any order__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2,2]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [4,9]
<strong>Explanation:</strong> [9,4] is also accepted.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums1.length, nums2.length &lt;= 1000 ``
*   `` 0 &lt;= nums1[i], nums2[i] &lt;= 1000 ``

&nbsp;

__Follow up:__

*   What if the given array is already sorted? How would you optimize your algorithm?
*   What if `` nums1 ``'s size is small compared to `` nums2 ``'s size? Which algorithm is better?
*   What if elements of `` nums2 `` are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?