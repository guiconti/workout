You have `` n `` super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any `` m `` (`` 1 &lt;= m &lt;= n ``) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time.

Given an integer array `` machines `` representing the number of dresses in each washing machine from left to right on the line, return _the minimum number of moves to make all the washing machines have the same number of dresses_. If it is not possible to do it, return `` -1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> machines = [1,0,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
1st move:    1     0 &lt;-- 5    =&gt;    1     1     4
2nd move:    1 &lt;-- 1 &lt;-- 4    =&gt;    2     1     3
3rd move:    2     1 &lt;-- 3    =&gt;    2     2     2
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> machines = [0,3,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
1st move:    0 &lt;-- 3     0    =&gt;    1     2     0
2nd move:    1     2 --&gt; 0    =&gt;    1     1     1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> machines = [0,2,0]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
It's impossible to make all three washing machines have the same number of dresses.
</pre>

&nbsp;

__Constraints:__

*   `` n == machines.length ``
*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= machines[i] &lt;= 10<sup>5</sup></code>