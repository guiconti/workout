You are given an `` m x n `` matrix `` M `` initialized with all `` 0 ``'s and an array of operations `` ops ``, where <code>ops[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> means `` M[x][y] `` should be incremented by one for all <code>0 &lt;= x &lt; a<sub>i</sub></code> and <code>0 &lt;= y &lt; b<sub>i</sub></code>.

Count and return _the number of maximum integers in the matrix after performing all the operations_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/ex1.jpg" style="width: 750px; height: 176px;"/>

<pre>
<strong>Input:</strong> m = 3, n = 3, ops = [[2,2],[3,3]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The maximum integer in M is 2, and there are four of it in M. So return 4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
<strong>Output:</strong> 4
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> m = 3, n = 3, ops = []
<strong>Output:</strong> 9
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= m, n &lt;= 4 * 10<sup>4</sup></code>
*   <code>1 &lt;= ops.length &lt;= 10<sup>4</sup></code>
*   `` ops[i].length == 2 ``
*   <code>1 &lt;= a<sub>i</sub> &lt;= m</code>
*   <code>1 &lt;= b<sub>i</sub> &lt;= n</code>