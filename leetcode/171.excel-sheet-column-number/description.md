Given a string `` columnTitle `` that represents the column title as appear in an Excel sheet, return _its corresponding column number_.

For example:

<pre>
A -&gt; 1
B -&gt; 2
C -&gt; 3
...
Z -&gt; 26
AA -&gt; 27
AB -&gt; 28 
...
</pre>

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> columnTitle = "A"
<strong>Output:</strong> 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> columnTitle = "AB"
<strong>Output:</strong> 28
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> columnTitle = "ZY"
<strong>Output:</strong> 701
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> columnTitle = "FXSHRXW"
<strong>Output:</strong> 2147483647
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= columnTitle.length &lt;= 7 ``
*   `` columnTitle `` consists only of uppercase English letters.
*   `` columnTitle `` is in the range `` ["A", "FXSHRXW"] ``.