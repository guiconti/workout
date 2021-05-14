You are given a string `` text ``. You should split it to k substrings <code>(subtext<sub>1</sub>, subtext<sub>2</sub>, ..., subtext<sub>k</sub>)</code> such that:

*   <code>subtext<sub>i</sub></code> is a __non-empty__ string.
*   The concatenation of all the substrings is equal to `` text `` (i.e., <code>subtext<sub>1</sub> + subtext<sub>2</sub> + ... + subtext<sub>k</sub> == text</code>).
*   <code>subtext<sub>i</sub> == subtext<sub>k - i + 1</sub></code> for all valid values of `` i `` (i.e., `` 1 &lt;= i &lt;= k ``).

Return the largest possible value of `` k ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> text = "ghiabcdefhelloadamhelloabcdefghi"
<strong>Output:</strong> 7
<strong>Explanation:</strong> We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> text = "merchant"
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can split the string on "(merchant)".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> text = "antaprezatepzapreanta"
<strong>Output:</strong> 11
<strong>Explanation:</strong> We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> text = "aaa"
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can split the string on "(a)(a)(a)".
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= text.length &lt;= 1000 ``
*   `` text `` consists only of lowercase English characters.