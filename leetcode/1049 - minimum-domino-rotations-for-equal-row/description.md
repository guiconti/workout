In a row of dominoes, `` A[i] `` and `` B[i] `` represent the top and bottom halves of the <code>i<sup>th</sup></code> domino.&nbsp; (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the <code>i<sup>th</sup></code> domino, so that `` A[i] `` and `` B[i] `` swap values.

Return the minimum number of rotations so that all the values in `` A `` are the same, or all the values in `` B ``&nbsp;are the same.

If it cannot be done, return `` -1 ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/03/08/domino.png" style="height: 161px; width: 200px;"/>

<pre>
<strong>Input:</strong> A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> A = [3,5,1,2,3], B = [3,6,3,3,4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= A.length == B.length &lt;= 2 * 10<sup>4</sup></code>
*   `` 1 &lt;= A[i], B[i] &lt;= 6 ``