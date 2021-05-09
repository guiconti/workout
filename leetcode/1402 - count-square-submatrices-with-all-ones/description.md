Given a `` m * n `` matrix of ones and zeros, return how many __square__ submatrices have all ones.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> matrix =
[
&nbsp; [0,1,1,1],
&nbsp; [1,1,1,1],
&nbsp; [0,1,1,1]
]
<strong>Output:</strong> 15
<strong>Explanation:</strong> 
There are <strong>10</strong> squares of side 1.
There are <strong>4</strong> squares of side 2.
There is  <strong>1</strong> square of side 3.
Total number of squares = 10 + 4 + 1 = <strong>15</strong>.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
There are <b>6</b> squares of side 1.  
There is <strong>1</strong> square of side 2. 
Total number of squares = 6 + 1 = <b>7</b>.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length&nbsp;&lt;= 300 ``
*   `` 1 &lt;= arr[0].length&nbsp;&lt;= 300 ``
*   `` 0 &lt;= arr[i][j] &lt;= 1 ``