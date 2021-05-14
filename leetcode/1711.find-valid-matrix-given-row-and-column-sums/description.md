You are given two arrays `` rowSum `` and `` colSum `` of non-negative integers where `` rowSum[i] `` is the sum of the elements in the <code>i<sup>th</sup></code> row and `` colSum[j] `` is the sum of the elements of the <code>j<sup>th</sup></code> column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of __non-negative__ integers of size `` rowSum.length x colSum.length `` that satisfies the `` rowSum `` and `` colSum `` requirements.

Return _a 2D array representing __any__ matrix that fulfills the requirements_. It's guaranteed that __at least one __matrix that fulfills the requirements exists.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> rowSum = [3,8], colSum = [4,7]
<strong>Output:</strong> [[3,0],
         [1,7]]
<strong>Explanation:</strong>
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> rowSum = [5,7,10], colSum = [8,6,8]
<strong>Output:</strong> [[0,5,0],
         [6,1,0],
         [2,0,8]]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> rowSum = [14,9], colSum = [6,9,8]
<strong>Output:</strong> [[0,9,5],
         [6,0,3]]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> rowSum = [1,0], colSum = [1]
<strong>Output:</strong> [[1],
         [0]]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> rowSum = [0], colSum = [0]
<strong>Output:</strong> [[0]]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= rowSum.length, colSum.length &lt;= 500 ``
*   <code>0 &lt;= rowSum[i], colSum[i] &lt;= 10<sup>8</sup></code>
*   `` sum(rows) == sum(columns) ``