Given an `` n x n `` binary matrix `` image ``, flip the image __horizontally__, then invert it, and return _the resulting image_.

To flip an image horizontally means that each row of the image is reversed.

*   For example, flipping `` [1,1,0] `` horizontally results in `` [0,1,1] ``.

To invert an image means that each `` 0 `` is replaced by `` 1 ``, and each `` 1 `` is replaced by `` 0 ``.

*   For example, inverting `` [0,1,1] `` results in `` [1,0,0] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> image = [[1,1,0],[1,0,1],[0,0,0]]
<strong>Output:</strong> [[1,0,0],[0,1,0],[1,1,1]]
<strong>Explanation:</strong> First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
<strong>Output:</strong> [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
<strong>Explanation:</strong> First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
</pre>

&nbsp;

__Constraints:__

*   `` n == image.length ``
*   `` n == image[i].length ``
*   `` 1 &lt;= n &lt;= 20 ``
*   `` images[i][j] `` is either `` 0 `` or `` 1 ``.