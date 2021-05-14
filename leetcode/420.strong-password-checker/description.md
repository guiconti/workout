A password is considered strong if the below conditions are all met:

*   It has at least `` 6 `` characters and at most `` 20 `` characters.
*   It contains at least __one lowercase__ letter, at least __one uppercase__ letter, and at least __one digit__.
*   It does&nbsp;not contain three repeating characters in a row (i.e.,&nbsp;`` "...aaa..." `` is weak, but `` "...aa...a..." `` is strong, assuming other conditions are met).

Given a string `` password ``, return _the minimum number of steps required to make `` password `` strong. if `` password `` is already strong, return `` 0 ``._

In one step, you can:

*   Insert one character to `` password ``,
*   Delete one character from `` password ``, or
*   Replace&nbsp;one character of `` password `` with another character.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> password = "a"
<strong>Output:</strong> 5
</pre>

__Example 2:__

<pre><strong>Input:</strong> password = "aA1"
<strong>Output:</strong> 3
</pre>

__Example 3:__

<pre><strong>Input:</strong> password = "1337C0d3"
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= password.length &lt;= 50 ``
*   `` password `` consists of letters, digits, dot&nbsp;`` '.' `` or exclamation mark `` '!' ``.