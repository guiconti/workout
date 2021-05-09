You are given a string `` s `` and an integer `` k ``, a `` k `` __duplicate removal__ consists of choosing `` k `` adjacent and equal letters from `` s `` and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make `` k `` __duplicate removals__ on `` s `` until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abcd", k = 2
<strong>Output:</strong> "abcd"
<strong>Explanation: </strong>There's nothing to delete.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "deeedbbcccbdaa", k = 3
<strong>Output:</strong> "aa"
<strong>Explanation: 
</strong>First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "pbbcggttciiippooaais", k = 2
<strong>Output:</strong> "ps"
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   <code>2 &lt;= k &lt;= 10<sup>4</sup></code>
*   `` s `` only contains lower case English letters.