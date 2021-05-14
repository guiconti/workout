You are given a string `` s `` that consists of lower case English letters and brackets.&nbsp;

Reverse the strings&nbsp;in each&nbsp;pair of matching parentheses, starting&nbsp;from the innermost one.

Your result should __not__ contain any brackets.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "(abcd)"
<strong>Output:</strong> "dcba"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "(u(love)i)"
<strong>Output:</strong> "iloveu"
<strong>Explanation:</strong>&nbsp;The substring "love" is reversed first, then the whole string is reversed.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "(ed(et(oc))el)"
<strong>Output:</strong> "leetcode"
<strong>Explanation:</strong>&nbsp;First, we reverse the substring "oc", then "etco", and finally, the whole string.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "a(bcdefghijkl(mno)p)q"
<strong>Output:</strong> "apmnolkjihgfedcbq"
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= s.length &lt;= 2000 ``
*   `` s `` only contains lower case English characters and parentheses.
*   It's guaranteed that all parentheses are balanced.