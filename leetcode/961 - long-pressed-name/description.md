Your friend is typing his `` name `` into a keyboard. Sometimes, when typing a character `` c ``, the key might get _long pressed_, and the character will be typed 1 or more times.

You examine the `` typed `` characters of the keyboard. Return `` True `` if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> name = "alex", typed = "aaleex"
<strong>Output:</strong> true
<strong>Explanation: </strong>'a' and 'e' in 'alex' were long pressed.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> name = "saeed", typed = "ssaaedd"
<strong>Output:</strong> false
<strong>Explanation: </strong>'e' must have been pressed twice, but it wasn't in the typed output.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> name = "leelee", typed = "lleeelee"
<strong>Output:</strong> true
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> name = "laiden", typed = "laiden"
<strong>Output:</strong> true
<strong>Explanation: </strong>It's not necessary to long press any character.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= name.length &lt;= 1000 ``
*   `` 1 &lt;= typed.length &lt;= 1000 ``
*   `` name `` and `` typed `` contain only lowercase English letters.