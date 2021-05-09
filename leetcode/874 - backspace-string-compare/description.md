Given two strings `` s `` and `` t ``, return `` true `` _if they are equal when both are typed into empty text editors_. `` '#' `` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "ab#c", t = "ad#c"
<strong>Output:</strong> true
<strong>Explanation:</strong> Both s and t become "ac".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "ab##", t = "c#d#"
<strong>Output:</strong> true
<strong>Explanation:</strong> Both s and t become "".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "a##c", t = "#a#c"
<strong>Output:</strong> true
<strong>Explanation:</strong> Both s and t become "c".
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "a#c", t = "b"
<strong>Output:</strong> false
<strong>Explanation:</strong> s becomes "c" while t becomes "b".
</pre>

&nbsp;

__Constraints:__

*   <code><span>1 &lt;= s.length, t.length &lt;= 200</span></code>
*   <span>`` s ``&nbsp;and `` t `` only contain&nbsp;lowercase letters and `` '#' `` characters.</span>

&nbsp;

__Follow up:__ Can you solve it in `` O(n) `` time and `` O(1) `` space?