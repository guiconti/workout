A string is a __valid parentheses string__ (denoted __VPS__) if it meets one of the following:

*   It is an empty string `` "" ``, or a single character not equal to `` "(" `` or `` ")" ``,
*   It can be written as `` AB `` (`` A `` concatenated with `` B ``), where `` A `` and `` B `` are __VPS__'s, or
*   It can be written as `` (A) ``, where `` A `` is a __VPS__.

We can similarly define the __nesting depth__ `` depth(S) `` of any VPS `` S `` as follows:

*   `` depth("") = 0 ``
*   `` depth(C) = 0 ``, where `` C `` is a string with a single character not equal to `` "(" `` or `` ")" ``.
*   `` depth(A + B) = max(depth(A), depth(B)) ``, where `` A `` and `` B `` are __VPS__'s.
*   `` depth("(" + A + ")") = 1 + depth(A) ``, where `` A `` is a __VPS__.

For example, `` "" ``, `` "()()" ``, and `` "()(()())" `` are __VPS__'s (with nesting depths 0, 1, and 2), and `` ")(" `` and `` "(()" `` are not __VPS__'s.

Given a __VPS__ represented as string `` s ``, return _the __nesting depth__ of _`` s ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "(1+(2*3)+((<u>8</u>)/4))+1"
<strong>Output:</strong> 3
<strong>Explanation:</strong> Digit 8 is inside of 3 nested parentheses in the string.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "(1)+((2))+(((<u>3</u>)))"
<strong>Output:</strong> 3
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "1+(<u>2</u>*3)/(2-1)"
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "<u>1</u>"
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 100 ``
*   `` s `` consists of digits `` 0-9 `` and characters `` '+' ``, `` '-' ``, `` '*' ``, `` '/' ``, `` '(' ``, and `` ')' ``.
*   It is guaranteed that parentheses expression `` s `` is a __VPS__.