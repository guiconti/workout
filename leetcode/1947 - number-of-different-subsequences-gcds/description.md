You are given an array `` nums `` that consists of positive integers.

The __GCD__ of a sequence of numbers is defined as the greatest integer that divides __all__ the numbers in the sequence evenly.

*   For example, the GCD of the sequence `` [4,6,16] `` is `` 2 ``.

A __subsequence__ of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

*   For example, `` [2,5,10] `` is a subsequence of <code>[1,2,1,<strong><u>2</u></strong>,4,1,<u><strong>5</strong></u>,<u><strong>10</strong></u>]</code>.

Return _the __number__ of __different__ GCDs among all __non-empty__ subsequences of_ `` nums ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/17/image-1.png" style="width: 149px; height: 309px;"/>

<pre>
<strong>Input:</strong> nums = [6,10,3]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The figure shows all the non-empty subsequences and their GCDs.
The different GCDs are 6, 10, 3, 2, and 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [5,15,40,5,6]
<strong>Output:</strong> 7
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 2 * 10<sup>5</sup></code>