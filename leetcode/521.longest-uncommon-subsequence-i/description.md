Given two strings `` a `` and `` b ``, return _the length of the __longest uncommon subsequence__ between _`` a `` _and_ `` b ``. If the longest uncommon subsequence does not exist, return `` -1 ``.

An __uncommon subsequence__ between two strings is a string that is a __subsequence of one but not the other__.

A __subsequence__ of a string `` s `` is a string that can be obtained after deleting any number of characters from `` s ``.

*   For example, `` "abc" `` is a subsequence of `` "aebdc" `` because you can delete the underlined characters in <code>"a<u>e</u>b<u>d</u>c"</code> to get `` "abc" ``. Other subsequences of `` "aebdc" `` include `` "aebdc" ``, `` "aeb" ``, and `` "" `` (empty string).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> a = "aba", b = "cdc"
<strong>Output:</strong> 3
<strong>Explanation:</strong> One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> a = "aaa", b = "bbb"
<strong>Output:</strong> 3
<strong>Explanation:</strong>&nbsp;The longest uncommon subsequences are "aaa" and "bbb".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> a = "aaa", b = "aaa"
<strong>Output:</strong> -1
<strong>Explanation:</strong>&nbsp;Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= a.length, b.length &lt;= 100 ``
*   `` a `` and `` b `` consist of lower-case English letters.