The __beauty__ of a string is the difference in frequencies between the most frequent and least frequent characters.

*   For example, the beauty of `` "abaacc" `` is `` 3 - 1 = 2 ``.

Given a string `` s ``, return _the sum of __beauty__ of all of its substrings._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "aabcb"
<strong>Output:</strong> 5
<strong>Explanation: </strong>The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aabcbaa"
<strong>Output:</strong> 17
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;=<sup> </sup>500</code>
*   `` s `` consists of only lowercase English letters.