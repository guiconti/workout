Given a string `` s ``, determine if it is __valid__.

A string `` s `` is __valid__ if, starting with an empty string `` t = "" ``, you can __transform __`` t ``__ into __`` s `` after performing the following operation __any number of times__:

*   Insert string `` "abc" `` into any position in `` t ``. More formally, `` t `` becomes <code>t<sub>left</sub> + "abc" + t<sub>right</sub></code>, where <code>t == t<sub>left</sub> + t<sub>right</sub></code>. Note that <code>t<sub>left</sub></code> and <code>t<sub>right</sub></code> may be __empty__.

Return `` true `` _if _`` s ``_ is a __valid__ string, otherwise, return_ `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "aabcbc"
<strong>Output:</strong> true
<strong>Explanation:</strong>
"" -&gt; "<u>abc</u>" -&gt; "a<u>abc</u>bc"
Thus, "aabcbc" is valid.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "abcabcababcc"
<strong>Output:</strong> true
<strong>Explanation:</strong>
"" -&gt; "<u>abc</u>" -&gt; "abc<u>abc</u>" -&gt; "abcabc<u>abc</u>" -&gt; "abcabcab<u>abc</u>c"
Thus, "abcabcababcc" is valid.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "abccba"
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to get "abccba" using the operation.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "cababc"
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to get "cababc" using the operation.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 2 * 10<sup>4</sup></code>
*   `` s `` consists of letters `` 'a' ``, `` 'b' ``, and `` 'c' ``