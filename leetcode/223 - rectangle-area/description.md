Given the coordinates of two __rectilinear__ rectangles in a 2D plane, return _the total area covered by the two rectangles_.

The first rectangle is defined by its __bottom-left__ corner `` (ax1, ay1) `` and its __top-right__ corner `` (ax2, ay2) ``.

The second rectangle is defined by its __bottom-left__ corner `` (bx1, by1) `` and its __top-right__ corner `` (bx2, by2) ``.

&nbsp;

__Example 1:__

<img alt="Rectangle Area" src="https://assets.leetcode.com/uploads/2021/05/08/rectangle-plane.png" style="width: 700px; height: 365px;"/>

<pre>
<strong>Input:</strong> ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
<strong>Output:</strong> 45
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
<strong>Output:</strong> 16
</pre>

&nbsp;

__Constraints:__

*   <code>-10<sup>4</sup> &lt;= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 &lt;= 10<sup>4</sup></code>