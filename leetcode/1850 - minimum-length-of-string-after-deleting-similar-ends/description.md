Given a string `` s `` consisting only of characters `` 'a' ``, `` 'b' ``, and `` 'c' ``. You are asked to apply the following algorithm on the string any number of times:

1.   Pick a __non-empty__ prefix from the string `` s `` where all the characters in the prefix are equal.
2.   Pick a __non-empty__ suffix from the string `` s `` where all the characters in this suffix are equal.
3.   The prefix and the suffix should not intersect at any index.
4.   The characters from the prefix and suffix must be the same.
5.   Delete both the prefix and the suffix.

Return _the __minimum length__ of _`` s `` _after performing the above operation any number of times (possibly zero times)_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "ca"
<strong>Output:</strong> 2
<strong>Explanation: </strong>You can't remove any characters, so the string stays as is.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "cabaabac"
<strong>Output:</strong> 0
<strong>Explanation:</strong> An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "aabccabba"
<strong>Output:</strong> 3
<strong>Explanation:</strong> An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s `` only consists of characters `` 'a' ``, `` 'b' ``, and `` 'c' ``.