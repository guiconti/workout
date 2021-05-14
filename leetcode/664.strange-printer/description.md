There is a strange printer with the following two special properties:

*   The printer can only print a sequence of __the same character__ each time.
*   At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

Given a string `` s ``, return _the minimum number of turns the printer needed to print it_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "aaabbb"
<strong>Output:</strong> 2
<strong>Explanation:</strong> Print "aaa" first and then print "bbb".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aba"
<strong>Output:</strong> 2
<strong>Explanation:</strong> Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 100 ``
*   `` s `` consists of lowercase English letters.