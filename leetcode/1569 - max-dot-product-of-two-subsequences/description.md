Given two arrays `` nums1 ``&nbsp;and <code><font face="monospace">nums2</font></code>

<font face="monospace">.</font>

Return the maximum dot product&nbsp;between&nbsp;__non-empty__ subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie,&nbsp;`` [2,3,5] ``&nbsp;is a subsequence of&nbsp;`` [1,2,3,4,5] ``&nbsp;while `` [1,5,3] ``&nbsp;is not).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums1 = [2,1,-2,5], nums2 = [3,0,-6]
<strong>Output:</strong> 18
<strong>Explanation:</strong> Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums1 = [3,-2], nums2 = [2,-6,7]
<strong>Output:</strong> 21
<strong>Explanation:</strong> Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums1 = [-1,-1], nums2 = [1,1]
<strong>Output:</strong> -1
<strong>Explanation: </strong>Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums1.length, nums2.length &lt;= 500 ``
*   `` -1000 &lt;= nums1[i], nums2[i] &lt;= 1000 ``