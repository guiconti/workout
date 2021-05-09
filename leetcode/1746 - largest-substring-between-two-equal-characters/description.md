Given a string `` s ``, return _the length of the longest substring between two equal characters, excluding the two characters._ If there is no such substring return `` -1 ``.

A __substring__ is a contiguous sequence of characters within a string.

&nbsp;

__Example 1:__

<strong>Input:</strong> s = "aa"
    <strong>Output:</strong> 0
    <strong>Explanation:</strong> The optimal substring here is an empty substring between the two 'a's.

__Example 2:__

<pre>
<strong>Input:</strong> s = "abca"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The optimal substring here is "bc".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "cbzxy"
<strong>Output:</strong> -1
<strong>Explanation:</strong> There are no characters that appear twice in s.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "cabbac"
<strong>Output:</strong> 4
<strong>Explanation:</strong> The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 300 ``
*   `` s `` contains only lowercase English letters.