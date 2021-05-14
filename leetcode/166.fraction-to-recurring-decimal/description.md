Given two integers representing the `` numerator `` and `` denominator `` of a fraction, return _the fraction in string format_.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return __any of them__.

It is __guaranteed__ that the length of the answer string is less than <code>10<sup>4</sup></code> for all the given inputs.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> numerator = 1, denominator = 2
<strong>Output:</strong> "0.5"
</pre>

__Example 2:__

<pre><strong>Input:</strong> numerator = 2, denominator = 1
<strong>Output:</strong> "2"
</pre>

__Example 3:__

<pre><strong>Input:</strong> numerator = 2, denominator = 3
<strong>Output:</strong> "0.(6)"
</pre>

__Example 4:__

<pre><strong>Input:</strong> numerator = 4, denominator = 333
<strong>Output:</strong> "0.(012)"
</pre>

__Example 5:__

<pre><strong>Input:</strong> numerator = 1, denominator = 5
<strong>Output:</strong> "0.2"
</pre>

&nbsp;

__Constraints:__

*   <code>-2<sup>31</sup> &lt;=&nbsp;numerator, denominator &lt;= 2<sup>31</sup> - 1</code>
*   `` denominator != 0 ``