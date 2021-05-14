__Balanced__ strings are those that have an equal quantity of `` 'L' `` and `` 'R' `` characters.

Given a __balanced__ string `` s ``, split it in the maximum amount of balanced strings.

Return _the maximum amount of split __balanced__ strings_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "RLRRLLRLRL"
<strong>Output:</strong> 4
<strong>Explanation: </strong>s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "RLLLLRRRLR"
<strong>Output:</strong> 3
<strong>Explanation: </strong>s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "LLLLRRRR"
<strong>Output:</strong> 1
<strong>Explanation: </strong>s can be split into "LLLLRRRR".
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "RLRRRLLRLL"
<strong>Output:</strong> 2
<strong>Explanation: </strong>s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 1000 ``
*   `` s[i] `` is either `` 'L' `` or `` 'R' ``.
*   `` s `` is a __balanced__ string.