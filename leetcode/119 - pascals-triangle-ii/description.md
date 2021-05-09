Given an integer `` rowIndex ``, return the <code>rowIndex<sup>th</sup></code> (__0-indexed__) row of the __Pascal's triangle__.

In __Pascal's triangle__, each number is the sum of the two numbers directly above it as shown:

<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px"/>

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> rowIndex = 3
<strong>Output:</strong> [1,3,3,1]
</pre>

__Example 2:__

<pre><strong>Input:</strong> rowIndex = 0
<strong>Output:</strong> [1]
</pre>

__Example 3:__

<pre><strong>Input:</strong> rowIndex = 1
<strong>Output:</strong> [1,1]
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= rowIndex &lt;= 33 ``

&nbsp;

__Follow up:__ Could you optimize your algorithm to use only `` O(rowIndex) `` extra space?