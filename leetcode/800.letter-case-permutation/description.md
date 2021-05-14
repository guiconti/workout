Given a string S, we can transform every letter individually&nbsp;to be lowercase or uppercase to create another string.

Return _a list of all possible strings we could create_. You can return the output&nbsp;in __any order__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> S = "a1b2"
<strong>Output:</strong> ["a1b2","a1B2","A1b2","A1B2"]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> S = "3z4"
<strong>Output:</strong> ["3z4","3Z4"]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> S = "12345"
<strong>Output:</strong> ["12345"]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> S = "0"
<strong>Output:</strong> ["0"]
</pre>

&nbsp;

__Constraints:__

*   `` S `` will be a string with length between `` 1 `` and `` 12 ``.
*   `` S `` will consist only of letters or digits.