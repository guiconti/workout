You are given two __sorted__ arrays of distinct integers `` nums1 `` and `` nums2. ``

A __valid___ ___path__ is defined as follows:

*   Choose&nbsp;array nums1 or nums2 to traverse (from index-0).
*   Traverse the current array from left to right.
*   If you are reading any value that is present in `` nums1 `` and `` nums2 ``&nbsp;you are allowed to change your path to the other array. (Only one repeated value is considered in the&nbsp;valid path).

_Score_ is defined as the sum of uniques values in a valid path.

Return the maximum _score_ you can obtain of all possible&nbsp;__valid&nbsp;paths__.

Since the answer&nbsp;may be too large,&nbsp;return it modulo&nbsp;10^9 + 7.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/07/16/sample_1_1893.png" style="width: 538px; height: 163px;"/></strong>

<pre>
<strong>Input:</strong> nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
<strong>Output:</strong> 30
<strong>Explanation:</strong>&nbsp;Valid paths:
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
The maximum is obtained with the path in green <strong>[2,4,6,8,10]</strong>.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums1 = [1,3,5,7,9], nums2 = [3,5,100]
<strong>Output:</strong> 109
<strong>Explanation:</strong>&nbsp;Maximum sum is obtained with the path <strong>[1,3,5,100]</strong>.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
<strong>Output:</strong> 40
<strong>Explanation:</strong>&nbsp;There are no common elements between nums1 and nums2.
Maximum sum is obtained with the path [6,7,8,9,10].
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]
<strong>Output:</strong> 61
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums1.length &lt;= 10^5 ``
*   `` 1 &lt;= nums2.length &lt;= 10^5 ``
*   `` 1 &lt;= nums1[i], nums2[i] &lt;= 10^7 ``
*   `` nums1 `` and `` nums2 `` are strictly increasing.