Given a&nbsp;`` rows x cols ``&nbsp;matrix&nbsp;`` mat ``,&nbsp;where `` mat[i][j] `` is either `` 0 `` or `` 1 ``,&nbsp;return _the number of special positions in `` mat ``._

A position `` (i,j) `` is called __special__&nbsp;if&nbsp;`` mat[i][j] == 1 `` and all other elements in row `` i ``&nbsp;and column `` j ``&nbsp;are `` 0 `` (rows and columns are __0-indexed__).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> mat = [[1,0,0],
&nbsp;             [0,0,<strong>1</strong>],
&nbsp;             [1,0,0]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> mat = [[<strong>1</strong>,0,0],
&nbsp;             [0,<strong>1</strong>,0],
&nbsp;             [0,0,<strong>1</strong>]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> (0,0), (1,1) and (2,2) are special positions. 
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> mat = [[0,0,0,<strong>1</strong>],
&nbsp;             [<strong>1</strong>,0,0,0],
&nbsp;             [0,1,1,0],
&nbsp;             [0,0,0,0]]
<strong>Output:</strong> 2
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> mat = [[0,0,0,0,0],
&nbsp;             [<strong>1</strong>,0,0,0,0],
&nbsp;             [0,<strong>1</strong>,0,0,0],
&nbsp;             [0,0,<strong>1</strong>,0,0],
&nbsp;             [0,0,0,1,1]]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   `` rows == mat.length ``
*   `` cols == mat[i].length ``
*   `` 1 &lt;= rows, cols &lt;= 100 ``
*   `` mat[i][j] `` is `` 0 `` or `` 1 ``.