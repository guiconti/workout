Given an integer array `` nums ``, return _the number of all the __arithmetic subsequences__ of_ `` nums ``.

A sequence of numbers is called arithmetic if it consists of __at least three elements__ and if the difference between any two consecutive elements is the same.

*   For example, `` [1, 3, 5, 7, 9] ``, `` [7, 7, 7, 7] ``, and `` [3, -1, -5, -9] `` are arithmetic sequences.
*   For example, `` [1, 1, 2, 5, 7] `` is not an arithmetic sequence.

A __subsequence__ of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

*   For example, `` [2,5,10] `` is a subsequence of <code>[1,2,1,<strong><u>2</u></strong>,4,1,<u><strong>5</strong></u>,<u><strong>10</strong></u>]</code>.

The answer is guaranteed to fit in __32-bit__ integer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,4,6,8,10]
<strong>Output:</strong> 7
<strong>Explanation:</strong> All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [7,7,7,7,7]
<strong>Output:</strong> 16
<strong>Explanation:</strong> Any subsequence of this array is arithmetic.
</pre>

&nbsp;

__Constraints:__

*   `` 1&nbsp; &lt;= nums.length &lt;= 1000 ``
*   <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>