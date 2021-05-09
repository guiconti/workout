Given an array of strings `` arr ``. String `` s `` is a concatenation of a sub-sequence of `` arr `` which have __unique characters__.

Return _the maximum possible length_ of `` s ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = ["un","iq","ue"]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = ["cha","r","act","ers"]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Possible solutions are "chaers" and "acters".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = ["abcdefghijklmnopqrstuvwxyz"]
<strong>Output:</strong> 26
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 16 ``
*   `` 1 &lt;= arr[i].length &lt;= 26 ``
*   `` arr[i] `` contains only lower case English letters.