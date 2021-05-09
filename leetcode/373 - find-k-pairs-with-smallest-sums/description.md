You are given two integer arrays `` nums1 `` and `` nums2 `` sorted in __ascending order__ and an integer `` k ``.

Define a pair `` (u, v) `` which consists of one element from the first array and one element from the second array.

Return _the_ `` k `` _pairs_ <code>(u<sub>1</sub>, v<sub>1</sub>), (u<sub>2</sub>, v<sub>2</sub>), ..., (u<sub>k</sub>, v<sub>k</sub>)</code> _with the smallest sums_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums1 = [1,7,11], nums2 = [2,4,6], k = 3
<strong>Output:</strong> [[1,2],[1,4],[1,6]]
<strong>Explanation:</strong> The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums1 = [1,1,2], nums2 = [1,2,3], k = 2
<strong>Output:</strong> [[1,1],[1,1]]
<strong>Explanation:</strong> The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3], k = 3
<strong>Output:</strong> [[1,3],[2,3]]
<strong>Explanation:</strong> All possible pairs are returned from the sequence: [1,3],[2,3]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>9</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup></code>
*   `` nums1 `` and `` nums2 `` both are sorted in __ascending order__.
*   `` 1 &lt;= k &lt;= 1000 ``