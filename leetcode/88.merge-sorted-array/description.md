Given two sorted integer arrays `` nums1 `` and `` nums2 ``, merge `` nums2 `` into `` nums1 `` as one sorted array.

The number of elements initialized in `` nums1 `` and `` nums2 `` are `` m `` and `` n `` respectively. You may assume that `` nums1 `` has a size equal to `` m + n `` such that it has enough space to hold additional elements from `` nums2 ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
<strong>Output:</strong> [1,2,2,3,5,6]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums1 = [1], m = 1, nums2 = [], n = 0
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

*   `` nums1.length == m + n ``
*   `` nums2.length == n ``
*   `` 0 &lt;= m, n &lt;= 200 ``
*   `` 1 &lt;= m + n &lt;= 200 ``
*   <code>-10<sup>9</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup></code>