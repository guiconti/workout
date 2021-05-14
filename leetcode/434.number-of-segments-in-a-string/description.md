You are given a string `` s ``, return _the number of segments in the string_.&nbsp;

A __segment__ is defined to be a contiguous sequence of __non-space characters__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "Hello, my name is John"
<strong>Output:</strong> 5
<strong>Explanation:</strong> The five segments are ["Hello,", "my", "name", "is", "John"]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "Hello"
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "love live! mu'sic forever"
<strong>Output:</strong> 4
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = ""
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= s.length &lt;= 300 ``
*   `` s `` consists of lower-case and upper-case English letters, digits or one of the following characters `` "!@#$%^&amp;*()_+-=',.:" ``.
*   The only space character in `` s `` is `` ' ' ``.