You are given two positive integer arrays `` nums1 `` and `` nums2 ``, both of length `` n ``.

The __absolute sum difference__ of arrays `` nums1 `` and `` nums2 `` is defined as the __sum__ of `` |nums1[i] - nums2[i]| `` for each `` 0 &lt;= i &lt; n `` (__0-indexed__).

You can replace __at most one__ element of `` nums1 `` with __any__ other element in `` nums1 `` to __minimize__ the absolute sum difference.

Return the _minimum absolute sum difference __after__ replacing at most one__ __element in the array `` nums1 ``._ Since the answer may be large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

`` |x| `` is defined as:

*   `` x `` if `` x &gt;= 0 ``, or
*   `` -x `` if `` x &lt; 0 ``.

&nbsp;

__Example 1:__

<strong>Input:</strong> nums1 = [1,7,5], nums2 = [2,3,5]
    <strong>Output:</strong> 3
    <strong>Explanation: </strong>There are two possible optimal solutions:
    - Replace the second element with the first: [1,<u><strong>7</strong></u>,5] =&gt; [1,<u><strong>1</strong></u>,5], or
    - Replace the second element with the third: [1,<u><strong>7</strong></u>,5] =&gt; [1,<u><strong>5</strong></u>,5].
    Both will yield an absolute sum difference of |1-2| + (|1-3| or |5-3|) + |5-5| = 3.

__Example 2:__

<pre>
<strong>Input:</strong> nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
<strong>Output:</strong> 0
<strong>Explanation: </strong>nums1 is equal to nums2 so no replacement is needed. This will result in an 
absolute sum difference of 0.
</pre>

__Example 3:__

<strong>Input:</strong> nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
    <strong>Output:</strong> 20
    <strong>Explanation: </strong>Replace the first element with the second: [<u><strong>1</strong></u>,10,4,4,2,7] =&gt; [<u><strong>10</strong></u>,10,4,4,2,7].
    This yields an absolute sum difference of |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20

&nbsp;

__Constraints:__

*   `` n == nums1.length ``
*   `` n == nums2.length ``
*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums1[i], nums2[i] &lt;= 10<sup>5</sup></code>