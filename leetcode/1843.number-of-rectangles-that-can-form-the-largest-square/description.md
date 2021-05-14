You are given an array `` rectangles `` where <code>rectangles[i] = [l<sub>i</sub>, w<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> rectangle of length <code>l<sub>i</sub></code> and width <code>w<sub>i</sub></code>.

You can cut the <code>i<sup>th</sup></code> rectangle to form a square with a side length of `` k `` if both <code>k &lt;= l<sub>i</sub></code> and <code>k &lt;= w<sub>i</sub></code>. For example, if you have a rectangle `` [4,6] ``, you can cut it to get a square with a side length of at most `` 4 ``.

Let `` maxLen `` be the side length of the __largest__ square you can obtain from any of the given rectangles.

Return _the __number__ of rectangles that can make a square with a side length of _`` maxLen ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> rectangles = [[5,8],[3,9],[5,12],[16,5]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> rectangles = [[2,3],[3,7],[4,3],[3,7]]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= rectangles.length &lt;= 1000 ``
*   `` rectangles[i].length == 2 ``
*   <code>1 &lt;= l<sub>i</sub>, w<sub>i</sub> &lt;= 10<sup>9</sup></code>
*   <code>l<sub>i</sub> != w<sub>i</sub></code>