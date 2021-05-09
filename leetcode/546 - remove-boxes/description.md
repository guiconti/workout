You are given several `` boxes `` with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of `` k `` boxes, `` k &gt;= 1 ``), remove them and get `` k * k `` points.

Return _the maximum points you can get_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> boxes = [1,3,2,2,2,3,4,3,1]
<strong>Output:</strong> 23
<strong>Explanation:</strong>
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----&gt; [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----&gt; [1, 3, 3, 3, 1] (1*1=1 points) 
----&gt; [1, 1] (3*3=9 points) 
----&gt; [] (2*2=4 points)
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> boxes = [1,1,1]
<strong>Output:</strong> 9
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> boxes = [1]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= boxes.length &lt;= 100 ``
*   `` 1 &lt;= boxes[i]&nbsp;&lt;= 100 ``