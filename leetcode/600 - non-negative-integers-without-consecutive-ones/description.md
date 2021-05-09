Given a positive integer `` n ``, return the number of the integers in the range `` [0, n] `` whose binary representations __do not__ contain consecutive ones.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong>
Here are the non-negative integers &lt;= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>9</sup></code>