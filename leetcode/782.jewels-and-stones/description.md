You're given strings `` jewels `` representing the types of stones that are jewels, and `` stones `` representing the stones you have. Each character in `` stones `` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `` "a" `` is considered a different type of stone from `` "A" ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> jewels = "aA", stones = "aAAbbbb"
<strong>Output:</strong> 3
</pre>

__Example 2:__

<pre><strong>Input:</strong> jewels = "z", stones = "ZZ"
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;=&nbsp;jewels.length, stones.length &lt;= 50 ``
*   `` jewels `` and `` stones `` consist of only English letters.
*   All the characters of&nbsp;`` jewels `` are __unique__.