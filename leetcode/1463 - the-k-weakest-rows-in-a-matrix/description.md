You are given an `` m x n `` binary matrix `` mat `` of `` 1 ``'s (representing soldiers) and `` 0 ``'s (representing civilians). The soldiers are positioned __in front__ of the civilians. That is, all the `` 1 ``'s will appear to the __left__ of all the `` 0 ``'s in each row.

A row `` i `` is __weaker__ than a row `` j `` if one of the following is true:

*   The number of soldiers in row `` i `` is less than the number of soldiers in row `` j ``.
*   Both rows have the same number of soldiers and `` i &lt; j ``.

Return _the indices of the _`` k ``_ __weakest__ rows in the matrix ordered from weakest to strongest_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
<strong>Output:</strong> [2,0,3]
<strong>Explanation:</strong> 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
<strong>Output:</strong> [0,2]
<strong>Explanation:</strong> 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
</pre>

&nbsp;

__Constraints:__

*   `` m == mat.length ``
*   `` n == mat[i].length ``
*   `` 2 &lt;= n, m &lt;= 100 ``
*   `` 1 &lt;= k &lt;= m ``
*   `` matrix[i][j] `` is either 0 or 1.