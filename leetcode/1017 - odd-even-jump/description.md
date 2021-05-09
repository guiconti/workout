You are given an integer array `` arr ``. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called __odd-numbered jumps__, and the (2nd, 4th, 6th, ...) jumps in the series are called __even-numbered jumps__. Note that the __jumps__ are numbered, not the indices.

You may jump forward from index `` i `` to index `` j `` (with `` i &lt; j ``) in the following way:

*   During __odd-numbered jumps__ (i.e., jumps 1, 3, 5, ...), you jump to the index `` j `` such that `` arr[i] &lt;= arr[j] `` and `` arr[j] `` is the smallest possible value. If there are multiple such indices `` j ``, you can only jump to the __smallest__ such index `` j ``.
*   During __even-numbered jumps__ (i.e., jumps 2, 4, 6, ...), you jump to the index `` j `` such that `` arr[i] &gt;= arr[j] `` and `` arr[j] `` is the largest possible value. If there are multiple such indices `` j ``, you can only jump to the __smallest__ such index `` j ``.
*   It may be the case that for some index `` i ``, there are no legal jumps.

A starting index is __good__ if, starting from that index, you can reach the end of the array (index `` arr.length - 1 ``) by jumping some number of times (possibly 0 or more than once).

Return _the number of __good__ starting indices_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [10,13,12,14,15]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
From starting index i = 4, we have reached the end already.
In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
jumps.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [2,3,1,1,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal to arr[0].
During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2] is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3
During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3] is the smallest value in [arr[3], arr[4]] that is greater than or equal to arr[2].
We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
number of jumps.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [5,1,3,4,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can reach the end from starting indices 1, 2, and 4.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr.length &lt;= 2 * 10<sup>4</sup></code>
*   <code>0 &lt;= arr[i] &lt; 10<sup>5</sup></code>