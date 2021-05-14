You own a __Goal Parser__ that can interpret a string `` command ``. The `` command `` consists of an alphabet of `` "G" ``, `` "()" `` and/or `` "(al)" `` in some order. The Goal Parser will interpret `` "G" `` as the string `` "G" ``, `` "()" `` as the string `` "o" ``, and `` "(al)" `` as the string `` "al" ``. The interpreted strings are then concatenated in the original order.

Given the string `` command ``, return _the __Goal Parser__'s interpretation of _`` command ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> command = "G()(al)"
<strong>Output:</strong> "Goal"
<strong>Explanation:</strong>&nbsp;The Goal Parser interprets the command as follows:
G -&gt; G
() -&gt; o
(al) -&gt; al
The final concatenated result is "Goal".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> command = "G()()()()(al)"
<strong>Output:</strong> "Gooooal"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> command = "(al)G(al)()()G"
<strong>Output:</strong> "alGalooG"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= command.length &lt;= 100 ``
*   `` command `` consists of `` "G" ``, `` "()" ``, and/or `` "(al)" `` in some order.