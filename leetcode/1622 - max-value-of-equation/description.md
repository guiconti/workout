Given an&nbsp;array `` points `` containing the coordinates of points on a 2D plane,&nbsp;sorted by the x-values, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;such that&nbsp;<code>x<sub>i</sub> &lt; x<sub>j</sub></code> for all `` 1 &lt;= i &lt; j &lt;= points.length ``. You are also given an integer&nbsp;`` k ``.

Find the _maximum value of the equation _<code>y<sub>i</sub>&nbsp;+ y<sub>j</sub>&nbsp;+ |x<sub>i</sub>&nbsp;- x<sub>j</sub>|</code>&nbsp;where <code>|x<sub>i</sub>&nbsp;- x<sub>j</sub>|&nbsp;&lt;= k</code>&nbsp;and `` 1 &lt;= i &lt; j &lt;= points.length ``. It is guaranteed that there exists at least one pair of points that satisfy the constraint <code>|x<sub>i</sub>&nbsp;- x<sub>j</sub>|&nbsp;&lt;= k</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> The first two points satisfy the condition |x<sub>i</sub>&nbsp;- x<sub>j</sub>| &lt;= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> points = [[0,0],[3,0],[9,2]], k = 3
<strong>Output:</strong> 3
<strong>Explanation: </strong>Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= points.length &lt;= 10^5 ``
*   `` points[i].length == 2 ``
*   `` -10^8&nbsp;&lt;= points[i][0], points[i][1] &lt;= 10^8 ``
*   `` 0 &lt;= k &lt;= 2 * 10^8 ``
*   `` points[i][0] &lt; points[j][0] ``&nbsp;for all&nbsp;`` 1 &lt;= i &lt; j &lt;= points.length ``
*   <code>x<sub>i</sub></code>&nbsp;form a strictly increasing sequence.