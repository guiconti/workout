Given two strings `` s `` and `` t ``, each of which represents a non-negative rational number, return `` true `` if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.

A __rational number__ can be represented using up to three parts: `` &lt;IntegerPart&gt; ``, `` &lt;NonRepeatingPart&gt; ``, and a `` &lt;RepeatingPart&gt; ``. The number will be represented in one of the following three ways:

*   `` &lt;IntegerPart&gt; ``
    
    *   For example, `` 12 ``, `` 0 ``, and `` 123 ``.
    
    
    
*   <code>&lt;IntegerPart&gt;<strong>&lt;.&gt;</strong>&lt;NonRepeatingPart&gt;</code>
    
    *   For example, `` 0.5 ``, `` 1. ``, `` 2.12 ``, and `` 123.0001 ``.
    
    
    
*   <code>&lt;IntegerPart&gt;<strong>&lt;.&gt;</strong>&lt;NonRepeatingPart&gt;<strong>&lt;(&gt;</strong>&lt;RepeatingPart&gt;<strong>&lt;)&gt;</strong></code>
    
    *   For example, `` 0.1(6) ``, `` 1.(9) ``, `` 123.00(1212) ``.
    
    
    

The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets. For example:

*   `` 1/6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66) ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "0.(52)", t = "0.5(25)"
<strong>Output:</strong> true
<strong>Explanation:</strong> Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "0.1666(6)", t = "0.166(66)"
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "0.9(9)", t = "1."
<strong>Output:</strong> true
<strong>Explanation:</strong> "0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [<a href="https://en.wikipedia.org/wiki/0.999..." target="_blank">See this link for an explanation.</a>]
"1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".
</pre>

&nbsp;

__Constraints:__

*   Each part consists only of digits.
*   The `` &lt;IntegerPart&gt; `` does not have leading zeros (except for the zero itself).
*   `` 1 &lt;= &lt;IntegerPart&gt;.length &lt;= 4 ``
*   `` 0 &lt;= &lt;NonRepeatingPart&gt;.length &lt;= 4 ``
*   `` 1 &lt;= &lt;RepeatingPart&gt;.length &lt;= 4 ``