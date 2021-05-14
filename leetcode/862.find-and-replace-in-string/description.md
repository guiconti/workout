To some string `` S ``, we will perform some&nbsp;replacement&nbsp;operations that replace groups of letters with new ones (not necessarily the same size).

Each replacement operation has `` 3 `` parameters: a starting index `` i ``, a source word&nbsp;`` x ``&nbsp;and a target word&nbsp;`` y ``.&nbsp; The rule is that if <code><font face="monospace">x</font></code>&nbsp;starts at position `` i ``&nbsp;in the __original__ __string__ __`` S ``__, then we will replace that occurrence of&nbsp;`` x ``&nbsp;with&nbsp;`` y ``.&nbsp; If not, we do nothing.

For example, if we have&nbsp;`` S = "abcd" ``&nbsp;and we have some replacement operation&nbsp;`` i = 2, x = "cd", y = "ffff" ``, then because&nbsp;`` "cd" ``&nbsp;starts at position <code><font face="monospace">2</font></code>&nbsp;in the original string `` S ``, we will replace it with `` "ffff" ``.

Using another example on `` S = "abcd" ``, if we have both the replacement operation `` i = 0, x = "ab", y = "eee" ``, as well as another replacement operation&nbsp;`` i = 2, x = "ec", y = "ffff" ``, this second operation does nothing because in the original string&nbsp;`` S[2] = 'c' ``, which doesn't match&nbsp;`` x[0] = 'e' ``.

All these operations occur simultaneously.&nbsp; It's guaranteed that there won't be any overlap in replacement: for example,&nbsp;`` S = "abc", indexes = [0, 1],&nbsp;sources = ["ab","bc"] `` is not a valid test case.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> S = "abcd", indexes = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
<strong>Output:</strong> "eeebffff"
<strong>Explanation:</strong>
"a" starts at index 0 in S, so it's replaced by "eee".
"cd" starts at index 2 in S, so it's replaced by "ffff".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> S = "abcd", indexes = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
<strong>Output:</strong> "eeecd"
<strong>Explanation:</strong>
"ab" starts at index 0 in S, so it's replaced by "eee".
"ec" doesn't starts at index 2 in the <strong>original</strong> S, so we do nothing.
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= S.length &lt;= 1000 ``
*   `` S `` consists of only lowercase English letters.
*   `` 0 &lt;= indexes.length &lt;= 100 ``
*   `` 0 &lt;= indexes[i] &lt; S.length ``
*   `` sources.length == indexes.length ``
*   `` targets.length == indexes.length ``
*   `` 1 &lt;= sources[i].length, targets[i].length &lt;= 50 ``
*   `` sources[i] ``&nbsp;and `` targets[i] ``&nbsp;consist of only lowercase English letters.