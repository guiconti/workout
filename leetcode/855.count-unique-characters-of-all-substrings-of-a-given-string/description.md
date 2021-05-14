Let's define a function `` countUniqueChars(s) ``&nbsp;that returns the number of unique characters on `` s ``, for example if `` s = "LEETCODE" ``&nbsp;then `` "L" ``, `` "T" ``,`` "C" ``,`` "O" ``,`` "D" `` are the unique characters since they appear only once in `` s ``, therefore&nbsp;`` countUniqueChars(s) = 5 ``.  
  
On this problem given a string `` s `` we need to return the sum of&nbsp;`` countUniqueChars(t) ``&nbsp;where `` t `` is a substring of `` s ``. Notice that some substrings can be repeated so on this case you have to count the repeated ones too.

Since the answer can be very large, return&nbsp;the answer&nbsp;modulo&nbsp;`` 10 ^ 9 + 7 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "ABC"
<strong>Output:</strong> 10
<strong>Explanation: </strong>All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
</pre>

__Example 2:__

<strong>Input:</strong> s = "ABA"
    <strong>Output:</strong> 8
    <strong>Explanation: </strong>The same as example 1, except countUniqueChars("ABA") = 1.

__Example 3:__

<pre>
<strong>Input:</strong> s = "LEETCODE"
<strong>Output:</strong> 92
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= s.length &lt;= 10^4 ``
*   `` s ``&nbsp;contain upper-case English letters only.