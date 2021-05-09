Given an array of strings `` words ``, return _the smallest string that contains each string in_ `` words `` _as a substring_. If there are multiple valid strings of the smallest length, return __any of them__.

You may assume that no string in `` words `` is a substring of another string in `` words ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["alex","loves","leetcode"]
<strong>Output:</strong> "alexlovesleetcode"
<strong>Explanation:</strong> All permutations of "alex","loves","leetcode" would also be accepted.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["catg","ctaagt","gcta","ttca","atgcatc"]
<strong>Output:</strong> "gctaagttcatgcatc"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 12 ``
*   `` 1 &lt;= words[i].length &lt;= 20 ``
*   `` words[i] `` consists of lowercase English letters.
*   All the strings of `` words `` are __unique__.