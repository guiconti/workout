Given two strings `` s `` and `` t ``, return _the minimum window in `` s `` which will contain all the characters in `` t ``_. If there is no such window in `` s `` that covers all characters in `` t ``, return _the empty string `` "" ``_.

__Note__ that If there is such a window, it is&nbsp;guaranteed that there will always be only one unique minimum window in `` s ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s = "ADOBECODEBANC", t = "ABC"
<strong>Output:</strong> "BANC"
</pre>

__Example 2:__

<pre><strong>Input:</strong> s = "a", t = "a"
<strong>Output:</strong> "a"
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length, t.length &lt;= 10<sup>5</sup></code>
*   `` s `` and `` t `` consist of English letters.

&nbsp;
__Follow up:__ Could you find an algorithm that runs in `` O(n) `` time?