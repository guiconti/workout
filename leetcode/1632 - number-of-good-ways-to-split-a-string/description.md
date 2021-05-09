You are given a string `` s ``, a&nbsp;split is called _good_&nbsp;if you can split&nbsp;`` s `` into 2&nbsp;non-empty strings `` p `` and `` q `` where its concatenation is equal to `` s `` and the number of distinct letters in `` p `` and `` q `` are the same.

Return the number of _good_ splits you can make in `` s ``.

&nbsp;

__Example 1:__

<strong>Input:</strong> s = "aacaba"
    <strong>Output:</strong> 2
    <strong>Explanation:</strong> There are 5 ways to split "aacaba" and 2 of them are good. 
    ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
    ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
    ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
    ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
    ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

__Example 2:__

<pre>
<strong>Input:</strong> s = "abcd"
<strong>Output:</strong> 1
<strong>Explanation: </strong>Split the string as follows ("ab", "cd").
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "aaaaa"
<strong>Output:</strong> 4
<strong>Explanation: </strong>All possible splits are good.</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "acbadbaada"
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` s `` contains only lowercase English letters.
*   `` 1 &lt;= s.length &lt;= 10^5 ``