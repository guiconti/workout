Given a string `` num `` that contains only digits and an integer `` target ``, return _all possibilities to add the binary operators_ `` '+' ``, `` '-' ``, _or_ `` '*' `` _between the digits of_ `` num `` _so that the resultant expression evaluates to the_ `` target `` _value_.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> num = "123", target = 6
<strong>Output:</strong> ["1*2*3","1+2+3"]
</pre>

__Example 2:__

<pre><strong>Input:</strong> num = "232", target = 8
<strong>Output:</strong> ["2*3+2","2+3*2"]
</pre>

__Example 3:__

<pre><strong>Input:</strong> num = "105", target = 5
<strong>Output:</strong> ["1*0+5","10-5"]
</pre>

__Example 4:__

<pre><strong>Input:</strong> num = "00", target = 0
<strong>Output:</strong> ["0*0","0+0","0-0"]
</pre>

__Example 5:__

<pre><strong>Input:</strong> num = "3456237490", target = 9191
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= num.length &lt;= 10 ``
*   `` num `` consists of only digits.
*   <code>-2<sup>31</sup> &lt;= target &lt;= 2<sup>31</sup> - 1</code>