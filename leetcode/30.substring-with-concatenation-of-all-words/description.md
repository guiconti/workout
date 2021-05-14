You are given a string `` s `` and an array of strings `` words `` of __the same length__. Return&nbsp;all starting indices of substring(s) in `` s ``&nbsp;that is a concatenation of each word in `` words `` __exactly once__, __in any order__,&nbsp;and __without any intervening characters__.

You can return the answer in __any order__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "barfoothefoobarman", words = ["foo","bar"]
<strong>Output:</strong> [0,9]
<strong>Explanation:</strong> Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
<strong>Output:</strong> [6,9,12]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>4</sup></code>
*   `` s `` consists of lower-case English letters.
*   `` 1 &lt;= words.length &lt;= 5000 ``
*   `` 1 &lt;= words[i].length &lt;= 30 ``
*   `` words[i] ``&nbsp;consists of lower-case English letters.