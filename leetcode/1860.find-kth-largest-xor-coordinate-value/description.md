You are given a 2D `` matrix `` of size `` m x n ``, consisting of non-negative integers. You are also given an integer `` k ``.

The __value__ of coordinate `` (a, b) `` of the matrix is the XOR of all `` matrix[i][j] `` where `` 0 &lt;= i &lt;= a &lt; m `` and `` 0 &lt;= j &lt;= b &lt; n `` __(0-indexed)__.

Find the <code>k<sup>th</sup></code> largest value __(1-indexed)__ of all the coordinates of `` matrix ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> matrix = [[5,2],[1,6]], k = 1
<strong>Output:</strong> 7
<strong>Explanation:</strong> The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> matrix = [[5,2],[1,6]], k = 2
<strong>Output:</strong> 5
<strong>Explanation: </strong>The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> matrix = [[5,2],[1,6]], k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.</pre>

__Example 4:__

<pre>
<strong>Input:</strong> matrix = [[5,2],[1,6]], k = 4
<strong>Output:</strong> 0
<strong>Explanation:</strong> The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which is the 4th largest value.</pre>

&nbsp;

__Constraints:__

*   `` m == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 &lt;= m, n &lt;= 1000 ``
*   <code>0 &lt;= matrix[i][j] &lt;= 10<sup>6</sup></code>
*   `` 1 &lt;= k &lt;= m * n ``