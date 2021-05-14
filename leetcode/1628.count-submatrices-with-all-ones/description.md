Given a&nbsp;`` rows * columns ``&nbsp;matrix `` mat `` of ones and zeros, return how many&nbsp;__submatrices__ have all ones.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> mat = [[1,0,1],
&nbsp;             [1,1,0],
&nbsp;             [1,1,0]]
<strong>Output:</strong> 13
<strong>Explanation:
</strong>There are <b>6</b> rectangles of side 1x1.
There are <b>2</b> rectangles of side 1x2.
There are <b>3</b> rectangles of side 2x1.
There is <b>1</b> rectangle of side 2x2. 
There is <b>1</b> rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = <strong>13.</strong>
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> mat = [[0,1,1,0],
&nbsp;             [0,1,1,1],
&nbsp;             [1,1,1,0]]
<strong>Output:</strong> 24
<strong>Explanation:</strong>
There are <b>8</b> rectangles of side 1x1.
There are <b>5</b> rectangles of side 1x2.
There are <b>2</b> rectangles of side 1x3. 
There are <b>4</b> rectangles of side 2x1.
There are <b>2</b> rectangles of side 2x2. 
There are <b>2</b> rectangles of side 3x1. 
There is <b>1</b> rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24<strong>.</strong>
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> mat = [[1,1,1,1,1,1]]
<strong>Output:</strong> 21
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> mat = [[1,0,1],[0,1,0],[1,0,1]]
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= rows&nbsp;&lt;= 150 ``
*   `` 1 &lt;= columns&nbsp;&lt;= 150 ``
*   `` 0 &lt;= mat[i][j] &lt;= 1 ``