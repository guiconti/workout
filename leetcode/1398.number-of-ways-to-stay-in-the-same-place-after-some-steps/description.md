You have a pointer at index `` 0 `` in an array of size <code><font face="monospace">arrLen</font></code>. At each step, you can move 1 position to the left, 1 position to the right&nbsp;in the array or stay in the same place&nbsp; (The pointer should not be placed outside the array at any time).

Given two integers&nbsp;`` steps `` and `` arrLen ``, return the number of&nbsp;ways such that your pointer still at index `` 0 `` after __exactly __<code><font face="monospace">steps</font></code>&nbsp;steps.

Since the answer&nbsp;may be too large,&nbsp;return it __modulo__&nbsp;`` 10^9 + 7 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> steps = 3, arrLen = 2
<strong>Output:</strong> 4
<strong>Explanation: </strong>There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> steps = 2, arrLen = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> steps = 4, arrLen = 2
<strong>Output:</strong> 8
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= steps &lt;= 500 ``
*   `` 1 &lt;= arrLen&nbsp;&lt;= 10^6 ``