In a string <code><font face="monospace">s</font></code>&nbsp;of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like `` s = "abbxxxxzyy" `` has the groups `` "a" ``, `` "bb" ``, `` "xxxx" ``, `` "z" ``, and&nbsp;`` "yy" ``.

A group is identified by an interval&nbsp;`` [start, end] ``, where&nbsp;`` start ``&nbsp;and&nbsp;`` end ``&nbsp;denote the start and end&nbsp;indices (inclusive) of the group. In the above example,&nbsp;`` "xxxx" ``&nbsp;has the interval&nbsp;`` [3,6] ``.

A group is considered&nbsp;__large__&nbsp;if it has 3 or more characters.

Return&nbsp;_the intervals of every __large__ group sorted in&nbsp;__increasing order by start index___.

&nbsp;

__Example 1:__

<strong>Input:</strong> s = "abbxxxxzzy"
    <strong>Output:</strong> [[3,6]]
    <strong>Explanation</strong>: "xxxx" is the only large group with start index 3 and end index 6.

__Example 2:__

<pre>
<strong>Input:</strong> s = "abc"
<strong>Output:</strong> []
<strong>Explanation</strong>: We have groups "a", "b", and "c", none of which are large groups.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "abcdddeeeeaabbbcd"
<strong>Output:</strong> [[3,5],[6,9],[12,14]]
<strong>Explanation</strong>: The large groups are "ddd", "eeee", and "bbb".
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "aba"
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 1000 ``
*   `` s `` contains lower-case English letters only.