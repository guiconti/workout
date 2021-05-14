There is an `` m x n `` matrix that is initialized to all `` 0 ``'s. There is also a 2D array `` indices `` where each <code>indices[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> represents a __0-indexed location__ to perform some increment operations on the matrix.

For each location `` indices[i] ``, do __both__ of the following:

1.   Increment __all__ the cells on row <code>r<sub>i</sub></code>.
2.   Increment __all__ the cells on column <code>c<sub>i</sub></code>.

Given `` m ``, `` n ``, and `` indices ``, return _the __number of odd-valued cells__ in the matrix after applying the increment to all locations in _`` indices ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/10/30/e1.png" style="width: 600px; height: 118px;"/>

<pre>
<strong>Input:</strong> m = 2, n = 3, indices = [[0,1],[1,1]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/10/30/e2.png" style="width: 600px; height: 150px;"/>

<pre>
<strong>Input:</strong> m = 2, n = 2, indices = [[1,1],[0,0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= m, n &lt;= 50 ``
*   `` 1 &lt;= indices.length &lt;= 100 ``
*   <code>0 &lt;= r<sub>i</sub> &lt; m</code>
*   <code>0 &lt;= c<sub>i</sub> &lt; n</code>

&nbsp;

__Follow up:__ Could you solve this in `` O(n + m + indices.length) `` time with only `` O(n + m) `` extra space?