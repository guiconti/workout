Given an integer `` num ``, repeatedly add all its digits until the result has only one digit, and return it.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = 38
<strong>Output:</strong> 2
<strong>Explanation:</strong> The process is
38 --&gt; 3 + 8 --&gt; 11
11 --&gt; 1 + 1 --&gt; 2 
Since 2 has only one digit, return it.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = 0
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>0 &lt;= num &lt;= 2<sup>31</sup> - 1</code>

&nbsp;

__Follow up:__ Could you do it without any loop/recursion in `` O(1) `` runtime?