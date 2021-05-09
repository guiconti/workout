Given an `` n x n `` `` matrix `` where each of the rows and columns are sorted in ascending order, return _the_ <code>k<sup>th</sup></code> _smallest element in the matrix_.

Note that it is the <code>k<sup>th</sup></code> smallest element __in the sorted order__, not the <code>k<sup>th</sup></code> __distinct__ element.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
<strong>Output:</strong> 13
<strong>Explanation:</strong> The elements in the matrix are [1,5,9,10,11,12,13,<u><strong>13</strong></u>,15], and the 8<sup>th</sup> smallest number is 13
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> matrix = [[-5]], k = 1
<strong>Output:</strong> -5
</pre>

&nbsp;

__Constraints:__

*   `` n == matrix.length ``
*   `` n == matrix[i].length ``
*   `` 1 &lt;= n &lt;= 300 ``
*   <code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code>
*   All the rows and columns of `` matrix `` are __guaranteed__ to be sorted in __non-decreasing order__.
*   <code>1 &lt;= k &lt;= n<sup>2</sup></code>