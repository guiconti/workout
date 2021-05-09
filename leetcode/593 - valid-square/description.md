Given the coordinates of four points in 2D space `` p1 ``, `` p2 ``, `` p3 `` and `` p4 ``, return `` true `` _if the four points construct a square_.

The coordinate of a point <code>p<sub>i</sub></code> is represented as <code>[x<sub>i</sub>, y<sub>i</sub>]</code>. The input is __not__ given in any order.

A __valid square__ has four equal sides with positive length and four equal angles (90-degree angles).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` p1.length == p2.length == p3.length == p4.length == 2 ``
*   <code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code>