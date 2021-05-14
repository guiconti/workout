We are given a 2-dimensional&nbsp;`` grid ``.&nbsp;`` "." `` is an empty cell, `` "#" `` is&nbsp;a wall, `` "@" `` is the starting point, (`` "a" ``, `` "b" ``, ...) are keys, and (`` "A" ``,&nbsp;`` "B" ``, ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.&nbsp; We cannot walk outside the grid, or walk into a wall.&nbsp; If we walk over a key, we pick it up.&nbsp; We can't walk over a lock unless we have the corresponding key.

For some 

<font face="monospace">1 &lt;= K &lt;= 6</font>

, there is exactly one lowercase and one uppercase letter of the first `` K `` letters of the English alphabet in the grid.&nbsp; This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were&nbsp;chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.&nbsp; If&nbsp;it's impossible, return `` -1 ``.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">["@.a.#","###.#","b.A.B"]</span>
<strong>Output: </strong><span id="example-output-1">8</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">["@..aA","..B#.","....b"]</span>
<strong>Output: </strong><span id="example-output-2">6</span>
</pre>
</div>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= grid.length&nbsp;&lt;= 30</code></li>
<li><code>1 &lt;= grid[0].length&nbsp;&lt;= 30</code></li>
<li><code>grid[i][j]</code> contains only<code> '.'</code>, <code>'#'</code>, <code>'@'</code>,&nbsp;<code>'a'-</code><code>'f</code><code>'</code> and <code>'A'-'F'</code></li>
<li>The number of keys is in <code>[1, 6]</code>.&nbsp; Each key has a different letter and opens exactly one lock.</li>
</ol>
</div>