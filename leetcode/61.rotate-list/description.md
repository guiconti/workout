Given the `` head `` of a linked&nbsp;list, rotate the list to the right by `` k `` places.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 600px; height: 254px;"/>

<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [4,5,1,2,3]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" style="width: 472px; height: 542px;"/>

<pre>
<strong>Input:</strong> head = [0,1,2], k = 4
<strong>Output:</strong> [2,0,1]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the list is in the range `` [0, 500] ``.
*   `` -100 &lt;= Node.val &lt;= 100 ``
*   <code>0 &lt;= k &lt;= 2 * 10<sup>9</sup></code>