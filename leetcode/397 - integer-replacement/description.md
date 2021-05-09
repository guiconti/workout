Given a positive integer `` n ``,&nbsp;you can apply one of the following&nbsp;operations:

1.   If `` n `` is even, replace `` n `` with `` n / 2 ``.
2.   If `` n `` is odd, replace `` n `` with either `` n + 1 `` or `` n - 1 ``.

Return _the minimum number of operations needed for `` n `` to become `` 1 ``_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 8
<strong>Output:</strong> 3
<strong>Explanation:</strong> 8 -&gt; 4 -&gt; 2 -&gt; 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> 4
<strong>Explanation: </strong>7 -&gt; 8 -&gt; 4 -&gt; 2 -&gt; 1
or 7 -&gt; 6 -&gt; 3 -&gt; 2 -&gt; 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code>