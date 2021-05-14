Given a circle represented as (`` radius ``, `` x_center ``, `` y_center ``)&nbsp;and an axis-aligned rectangle represented as (`` x1 ``, `` y1 ``, `` x2 ``, `` y2 ``),&nbsp;where (`` x1 ``, `` y1 ``) are the coordinates of the bottom-left corner, and (`` x2 ``, `` y2 ``) are the coordinates of the top-right corner of the&nbsp;rectangle.

Return True if the circle and rectangle are overlapped otherwise return False.

In other words, check if there are __any __point&nbsp;(xi, yi) such that belongs to the circle and the rectangle at the same time.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/20/sample_4_1728.png" style="width: 258px; height: 167px;"/>

<pre>
<strong>Input:</strong> radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> Circle and rectangle share the point (1,0) 
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/02/20/sample_2_1728.png" style="width: 150px; height: 135px;"/></strong>

<pre>
<strong>Input:</strong> radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
<strong>Output:</strong> true
</pre>

__Example 3:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/03/03/sample_6_1728.png" style="width: 175px; height: 165px;"/></strong>

<pre>
<strong>Input:</strong> radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
<strong>Output:</strong> true
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= radius &lt;= 2000 ``
*   `` -10^4 &lt;= x_center, y_center, x1, y1, x2, y2 &lt;= 10^4 ``
*   `` x1 &lt; x2 ``
*   `` y1 &lt; y2 ``