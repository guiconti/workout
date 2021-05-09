You are given a string `` s ``, and an array of pairs of indices in the string&nbsp;`` pairs ``&nbsp;where&nbsp;`` pairs[i] =&nbsp;[a, b] ``&nbsp;indicates 2 indices(0-indexed) of the string.

You can&nbsp;swap the characters at any pair of indices in the given&nbsp;`` pairs ``&nbsp;__any number of times__.

Return the&nbsp;lexicographically smallest string that `` s ``&nbsp;can be changed to after using the swaps.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "dcab", pairs = [[0,3],[1,2]]
<strong>Output:</strong> "bacd"
<strong>Explaination:</strong> 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "dcab", pairs = [[0,3],[1,2],[0,2]]
<strong>Output:</strong> "abcd"
<strong>Explaination: </strong>
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "cba", pairs = [[0,1],[1,2]]
<strong>Output:</strong> "abc"
<strong>Explaination: </strong>
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 10^5 ``
*   `` 0 &lt;= pairs.length &lt;= 10^5 ``
*   `` 0 &lt;= pairs[i][0], pairs[i][1] &lt;&nbsp;s.length ``
*   `` s ``&nbsp;only contains lower case English letters.