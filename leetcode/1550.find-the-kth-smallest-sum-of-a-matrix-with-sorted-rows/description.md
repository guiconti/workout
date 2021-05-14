You are given an&nbsp;`` m&nbsp;* n ``&nbsp;matrix,&nbsp;`` mat ``, and an integer `` k ``,&nbsp;which&nbsp;has its rows sorted in non-decreasing&nbsp;order.

You are allowed to choose exactly 1 element from each row to form an array.&nbsp;Return the Kth __smallest__ array sum among all possible arrays.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> mat = [[1,3,11],[2,4,6]], k = 5
<strong>Output:</strong> 7
<strong>Explanation: </strong>Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  </pre>

__Example 2:__

<pre>
<strong>Input:</strong> mat = [[1,3,11],[2,4,6]], k = 9
<strong>Output:</strong> 17
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
<strong>Output:</strong> 9
<strong>Explanation:</strong> Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> mat = [[1,1,10],[2,2,9]], k = 7
<strong>Output:</strong> 12
</pre>

&nbsp;

__Constraints:__

*   `` m == mat.length ``
*   `` n == mat.length[i] ``
*   `` 1 &lt;= m, n &lt;= 40 ``
*   `` 1 &lt;= k &lt;= min(200, n ^&nbsp;m) ``
*   `` 1 &lt;= mat[i][j] &lt;= 5000 ``
*   `` mat[i] `` is a non decreasing array.