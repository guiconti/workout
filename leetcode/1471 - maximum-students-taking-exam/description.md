Given a `` m&nbsp;* n ``&nbsp;matrix `` seats ``&nbsp;&nbsp;that represent seats distributions&nbsp;in a classroom.&nbsp;If a seat&nbsp;is&nbsp;broken, it is denoted by `` '#' `` character otherwise it is denoted by a `` '.' `` character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting&nbsp;directly in front or behind him. Return the __maximum __number of students that can take the exam together&nbsp;without any cheating being possible..

Students must be placed in seats in good condition.

&nbsp;

__Example 1:__

<img height="200" src="https://assets.leetcode.com/uploads/2020/01/29/image.png" width="339"/>

<pre>
<strong>Input:</strong> seats = [["#",".","#","#",".","#"],
&nbsp;               [".","#","#","#","#","."],
&nbsp;               ["#",".","#","#",".","#"]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Teacher can place 4 students in available seats so they don't cheat on the exam. 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> seats = [[".","#"],
&nbsp;               ["#","#"],
&nbsp;               ["#","."],
&nbsp;               ["#","#"],
&nbsp;               [".","#"]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Place all students in available seats. 

</pre>

__Example 3:__

<pre>
<strong>Input:</strong> seats = [["#",".","<strong>.</strong>",".","#"],
&nbsp;               ["<strong>.</strong>","#","<strong>.</strong>","#","<strong>.</strong>"],
&nbsp;               ["<strong>.</strong>",".","#",".","<strong>.</strong>"],
&nbsp;               ["<strong>.</strong>","#","<strong>.</strong>","#","<strong>.</strong>"],
&nbsp;               ["#",".","<strong>.</strong>",".","#"]]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Place students in available seats in column 1, 3 and 5.
</pre>

&nbsp;

__Constraints:__

<ul><li><code>seats</code>&nbsp;contains only characters&nbsp;<code>'.'<font face="sans-serif, Arial, Verdana, Trebuchet MS">&nbsp;and</font></code><code>'#'.</code></li><li><code>m ==&nbsp;seats.length</code></li><li><code>n ==&nbsp;seats[i].length</code></li><li><code>1 &lt;= m &lt;= 8</code></li><li><code>1 &lt;= n &lt;= 8</code></li></ul>