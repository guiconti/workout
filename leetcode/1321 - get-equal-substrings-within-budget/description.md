You are given two strings `` s `` and `` t `` of the same length. You want to change `` s `` to `` t ``. Changing the `` i ``-th character of `` s `` to `` i ``-th character of `` t `` costs `` |s[i] - t[i]| `` that is, the absolute difference between the ASCII values of the characters.

You are also given an integer `` maxCost ``.

Return the maximum length of a substring of `` s `` that can be changed to be the same as the corresponding substring of `` t ``with a cost less than or equal to `` maxCost ``.

If there is no substring from&nbsp;`` s `` that can be changed to its corresponding substring from `` t ``, return `` 0 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abcd", t = "bcdf", maxCost = 3
<strong>Output:</strong> 3
<strong>Explanation: </strong>"abc" of s can change to "bcd". That costs 3, so the maximum length is 3.</pre>

__Example 2:__

<strong>Input:</strong> s = "abcd", t = "cdef", maxCost = 3
    <strong>Output:</strong> 1
    <strong>Explanation: </strong>Each character in s costs 2 to change to charactor in t, so the maximum length is 1.

__Example 3:__

<pre>
<strong>Input:</strong> s = "abcd", t = "acde", maxCost = 0
<strong>Output:</strong> 1
<strong>Explanation: </strong>You can't make any change, so the maximum length is 1.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length, t.length &lt;= 10^5 ``
*   `` 0 &lt;= maxCost &lt;= 10^6 ``
*   `` s `` and&nbsp;`` t `` only contain lower case English letters.