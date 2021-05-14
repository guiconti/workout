Given a square grid&nbsp;of integers&nbsp;`` arr ``, a _falling path with non-zero shifts_&nbsp;is a choice of&nbsp;exactly one element from each row of `` arr ``, such that no two elements chosen in adjacent rows are in&nbsp;the same column.

Return the&nbsp;minimum&nbsp;sum of a falling path with non-zero shifts.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> 13
<strong>Explanation: </strong>
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is&nbsp;[1,5,7], so the answer is&nbsp;13.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length == arr[i].length &lt;= 200 ``
*   `` -99 &lt;= arr[i][j] &lt;= 99 ``