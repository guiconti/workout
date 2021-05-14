The Leetcode file system keeps a log each time some user performs a _change folder_ operation.

The operations are described below:

*   `` "../" `` : Move to the parent folder of the current folder. (If you are already in the main folder, __remain in the same folder__).
*   `` "./" `` : Remain in the same folder.
*   `` "x/" `` : Move to the child folder named `` x `` (This folder is __guaranteed to always exist__).

You are given a list of strings `` logs `` where `` logs[i] `` is the operation performed by the user at the <code>i<sup>th</sup></code> step.

The file system starts in the main folder, then the operations in `` logs `` are performed.

Return _the minimum number of operations needed to go back to the main folder after the change folder operations._

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/sample_11_1957.png" style="width: 775px; height: 151px;"/>

<pre>
<strong>Input:</strong> logs = ["d1/","d2/","../","d21/","./"]
<strong>Output:</strong> 2
<strong>Explanation: </strong>Use this change folder operation "../" 2 times and go back to the main folder.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/sample_22_1957.png" style="width: 600px; height: 270px;"/>

<pre>
<strong>Input:</strong> logs = ["d1/","d2/","./","d3/","../","d31/"]
<strong>Output:</strong> 3
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> logs = ["d1/","../","../","../"]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= logs.length &lt;= 10<sup>3</sup></code>
*   `` 2 &lt;= logs[i].length &lt;= 10 ``
*   `` logs[i] `` contains lowercase English letters, digits, `` '.' ``, and `` '/' ``.
*   `` logs[i] `` follows the format described in the statement.
*   Folder names consist of lowercase English letters and digits.