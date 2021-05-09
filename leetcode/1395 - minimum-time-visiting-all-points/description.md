On a 2D plane, there are `` n `` points with integer coordinates <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>. Return _the __minimum time__ in seconds to visit all the points in the order given by _`` points ``.

You can move according to these rules:

*   In `` 1 `` second, you can either:	
    
    *   move vertically by one&nbsp;unit,
    *   move horizontally by one unit, or
    *   move diagonally `` sqrt(2) `` units (in other words, move one unit vertically then one unit horizontally in `` 1 `` second).
    
    
    
*   You have to visit the points in the same order as they appear in the array.
*   You are allowed to pass through points that appear later in the order, but these do not count as visits.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/1626_example_1.PNG" style="width: 500px; height: 428px;"/>

<pre>
<strong>Input:</strong> points = [[1,1],[3,4],[-1,0]]
<strong>Output:</strong> 7
<strong>Explanation: </strong>One optimal path is <strong>[1,1]</strong> -&gt; [2,2] -&gt; [3,3] -&gt; <strong>[3,4] </strong>-&gt; [2,3] -&gt; [1,2] -&gt; [0,1] -&gt; <strong>[-1,0]</strong>   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds</pre>

__Example 2:__

<pre>
<strong>Input:</strong> points = [[3,2],[-2,2]]
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   `` points.length == n ``
*   `` 1 &lt;= n&nbsp;&lt;= 100 ``
*   `` points[i].length == 2 ``
*   `` -1000&nbsp;&lt;= points[i][0], points[i][1]&nbsp;&lt;= 1000 ``