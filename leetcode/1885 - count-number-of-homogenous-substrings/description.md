Given a string `` s ``, return _the number of __homogenous__ substrings of _`` s ``_._ Since the answer may be too large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

A string is __homogenous__ if all the characters of the string are the same.

A __substring__ is a contiguous sequence of characters within a string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abbcccaa"
<strong>Output:</strong> 13
<strong>Explanation:</strong> The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "xy"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The homogenous substrings are "x" and "y".</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "zzzzz"
<strong>Output:</strong> 15
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s `` consists of lowercase letters.