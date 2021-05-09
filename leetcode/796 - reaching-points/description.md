A move consists of taking a point `` (x, y) `` and transforming it to either `` (x, x+y) `` or `` (x+y, y) ``.

Given a starting point `` (sx, sy) `` and a target point `` (tx, ty) ``, return `` True `` if and only if a sequence of moves exists to transform the point `` (sx, sy) `` to `` (tx, ty) ``. Otherwise, return `` False ``.

<pre>
<strong>Examples:</strong>
<strong>Input:</strong> sx = 1, sy = 1, tx = 3, ty = 5
<strong>Output:</strong> True
<strong>Explanation:</strong>
One series of moves that transforms the starting point to the target is:
(1, 1) -&gt; (1, 2)
(1, 2) -&gt; (3, 2)
(3, 2) -&gt; (3, 5)

<strong>Input:</strong> sx = 1, sy = 1, tx = 2, ty = 2
<strong>Output:</strong> False

<strong>Input:</strong> sx = 1, sy = 1, tx = 1, ty = 1
<strong>Output:</strong> True

</pre>

__Note:__

*   `` sx, sy, tx, ty `` will all be integers in the range `` [1, 10^9] ``.