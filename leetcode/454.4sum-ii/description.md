Given four integer arrays `` nums1 ``, `` nums2 ``, `` nums3 ``, and `` nums4 `` all of length `` n ``, return the number of tuples `` (i, j, k, l) `` such that:

*   `` 0 &lt;= i, j, k, l &lt; n ``
*   `` nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0 ``

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The two tuples are:
1. (0, 0, 0, 1) -&gt; nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -&gt; nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` n == nums1.length ``
*   `` n == nums2.length ``
*   `` n == nums3.length ``
*   `` n == nums4.length ``
*   `` 1 &lt;= n &lt;= 200 ``
*   <code>-2<sup>28</sup> &lt;= nums1[i], nums2[i], nums3[i], nums4[i] &lt;= 2<sup>28</sup></code>