Given two arrays of integers&nbsp;`` nums1 `` and `` nums2 ``, return the number of triplets formed (type 1 and type 2) under the following rules:

*   Type 1: Triplet (i, j, k)&nbsp;if <code>nums1[i]<sup>2</sup>&nbsp;== nums2[j] * nums2[k]</code> where `` 0 &lt;= i &lt; nums1.length `` and `` 0 &lt;= j &lt; k &lt; nums2.length ``.
*   Type 2:&nbsp;Triplet (i, j, k) if <code>nums2[i]<sup>2</sup>&nbsp;== nums1[j] * nums1[k]</code> where `` 0 &lt;= i &lt; nums2.length `` and `` 0 &lt;= j &lt; k &lt; nums1.length ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums1 = [7,4], nums2 = [5,2,8,9]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8). 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums1 = [1,1], nums2 = [1,1,1]
<strong>Output:</strong> 9
<strong>Explanation:</strong> All Triplets are valid, because 1^2 = 1 * 1.
Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 = nums2[j] * nums2[k].
Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums1 = [7,7,8,3], nums2 = [1,2,9,7]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 valid triplets.
Type 1: (3,0,2).  nums1[3]^2 = nums2[0] * nums2[2].
Type 2: (3,0,1).  nums2[3]^2 = nums1[0] * nums1[1].
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no valid triplets.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums1.length, nums2.length &lt;= 1000 ``
*   `` 1 &lt;= nums1[i], nums2[i] &lt;= 10^5 ``