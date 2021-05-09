You are given a string `` allowed `` consisting of __distinct__ characters and an array of strings `` words ``. A string is __consistent __if all characters in the string appear in the string `` allowed ``.

Return_ the number of __consistent__ strings in the array _`` words ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
<strong>Output:</strong> 7
<strong>Explanation:</strong> All strings are consistent.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Strings "cc", "acd", "ac", and "d" are consistent.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= words.length &lt;= 10<sup>4</sup></code>
*   <code>1 &lt;= allowed.length &lt;=<sup> </sup>26</code>
*   `` 1 &lt;= words[i].length &lt;= 10 ``
*   The characters in `` allowed `` are __distinct__.
*   `` words[i] `` and `` allowed `` contain only lowercase English letters.