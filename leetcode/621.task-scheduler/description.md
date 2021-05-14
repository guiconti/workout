Given a characters array `` tasks ``, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer&nbsp;`` n `` that represents the cooldown period between&nbsp;two __same tasks__&nbsp;(the same letter in the array), that is that there must be at least `` n `` units of time between any two same tasks.

Return _the least number of units of times that the CPU will take to finish all the given tasks_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> tasks = ["A","A","A","B","B","B"], n = 2
<strong>Output:</strong> 8
<strong>Explanation:</strong> 
A -&gt; B -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; A -&gt; B
There is at least 2 units of time between any two same tasks.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> tasks = ["A","A","A","B","B","B"], n = 0
<strong>Output:</strong> 6
<strong>Explanation:</strong> On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
<strong>Output:</strong> 16
<strong>Explanation:</strong> 
One possible solution is
A -&gt; B -&gt; C -&gt; A -&gt; D -&gt; E -&gt; A -&gt; F -&gt; G -&gt; A -&gt; idle -&gt; idle -&gt; A -&gt; idle -&gt; idle -&gt; A
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= task.length &lt;= 10<sup>4</sup></code>
*   `` tasks[i] `` is upper-case English letter.
*   The integer `` n `` is in the range `` [0, 100] ``.