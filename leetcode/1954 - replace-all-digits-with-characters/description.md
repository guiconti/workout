You are given a __0-indexed__ string `` s `` that has lowercase English letters in its __even__ indices and digits in its __odd__ indices.

There is a function `` shift(c, x) ``, where `` c `` is a character and `` x `` is a digit, that returns the <code>x<sup>th</sup></code> character after `` c ``.

*   For example, `` shift('a', 5) = 'f' `` and `` shift('x', 0) = 'x' ``.

For every __odd__&nbsp;index `` i ``, you want to replace the digit `` s[i] `` with `` shift(s[i-1], s[i]) ``.

Return `` s ``_ after replacing all digits. It is __guaranteed__ that _`` shift(s[i-1], s[i]) ``_ will never exceed _`` 'z' ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "a1c1e1"
<strong>Output:</strong> "abcdef"
<strong>Explanation: </strong>The digits are replaced as follows:
- s[1] -&gt; shift('a',1) = 'b'
- s[3] -&gt; shift('c',1) = 'd'
- s[5] -&gt; shift('e',1) = 'f'</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "a1b2c3d4e"
<strong>Output:</strong> "abbdcfdhe"
<strong>Explanation: </strong>The digits are replaced as follows:
- s[1] -&gt; shift('a',1) = 'b'
- s[3] -&gt; shift('b',2) = 'd'
- s[5] -&gt; shift('c',3) = 'f'
- s[7] -&gt; shift('d',4) = 'h'</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 100 ``
*   `` s `` consists only of lowercase English letters and digits.
*   `` shift(s[i-1], s[i]) &lt;= 'z' `` for all __odd__ indices `` i ``.