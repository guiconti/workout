You are given `` k `` identical eggs and you have access to a building with `` n `` floors labeled from `` 1 `` to `` n ``.

You know that there exists a floor `` f `` where `` 0 &lt;= f &lt;= n `` such that any egg dropped at a floor __higher__ than `` f `` will __break__, and any egg dropped __at or below__ floor `` f `` will __not break__.

Each move, you may take an unbroken egg and drop it from any floor `` x `` (where `` 1 &lt;= x &lt;= n ``). If the egg breaks, you can no longer use it. However, if the egg does not break, you may __reuse__ it in future moves.

Return _the __minimum number of moves__ that you need to determine __with certainty__ what the value of _`` f `` is.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> k = 1, n = 2
<strong>Output:</strong> 2
<strong>Explanation: </strong>
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> k = 2, n = 6
<strong>Output:</strong> 3
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> k = 3, n = 14
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= k &lt;= 100 ``
*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>