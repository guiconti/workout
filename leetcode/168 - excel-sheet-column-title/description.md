Given an integer `` columnNumber ``, return _its corresponding column title as it appears in an Excel sheet_.

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
<strong>Input:</strong> columnNumber = 1
<strong>Output:</strong> "A"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> columnNumber = 28
<strong>Output:</strong> "AB"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> columnNumber = 701
<strong>Output:</strong> "ZY"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> columnNumber = 2147483647
<strong>Output:</strong> "FXSHRXW"
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= columnNumber &lt;= 2<sup>31</sup> - 1</code>