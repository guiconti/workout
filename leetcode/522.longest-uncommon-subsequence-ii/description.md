Given an array of strings `` strs ``, return _the length of the __longest uncommon subsequence__ between them_. If the longest uncommon subsequence does not exist, return `` -1 ``.

An __uncommon subsequence__ between an array of strings is a string that is a __subsequence of one string but not the others__.

A __subsequence__ of a string `` s `` is a string that can be obtained after deleting any number of characters from `` s ``.

*   For example, `` "abc" `` is a subsequence of `` "aebdc" `` because you can delete the underlined characters in <code>"a<u>e</u>b<u>d</u>c"</code> to get `` "abc" ``. Other subsequences of `` "aebdc" `` include `` "aebdc" ``, `` "aeb" ``, and `` "" `` (empty string).

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> strs = ["aba","cdc","eae"]
<strong>Output:</strong> 3
</pre>

__Example 2:__

<pre><strong>Input:</strong> strs = ["aaa","aaa","aa"]
<strong>Output:</strong> -1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= strs.length &lt;= 50 ``
*   `` 1 &lt;= strs[i].length &lt;= 10 ``
*   `` strs[i] `` consists of lowercase English letters.