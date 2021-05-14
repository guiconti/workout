In a given 2D binary array `` A ``, there are two islands.&nbsp; (An island is a 4-directionally connected group of&nbsp;`` 1 ``s not connected to any other 1s.)

Now, we may change `` 0 ``s to `` 1 ``s so as to connect the two islands together to form 1 island.

Return the smallest number of `` 0 ``s that must be flipped.&nbsp; (It is guaranteed that the answer is at least 1.)

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> A = [[0,1],[1,0]]
<strong>Output:</strong> 1
</pre>

__Example 2:__

<pre><strong>Input:</strong> A = [[0,1,0],[0,0,0],[0,0,1]]
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre><strong>Input:</strong> A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= A.length == A[0].length &lt;= 100 ``
*   `` A[i][j] == 0 `` or `` A[i][j] == 1 ``