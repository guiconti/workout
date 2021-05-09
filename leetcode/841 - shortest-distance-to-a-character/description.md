Given a string `` s `` and a character `` c `` that occurs in `` s ``, return _an array of integers _`` answer ``_ where _`` answer.length == s.length ``_ and _`` answer[i] ``_ is the __distance__ from index _`` i ``_ to the __closest__ occurrence of character _`` c ``_ in _`` s ``.

The __distance__ between two indices `` i `` and `` j `` is `` abs(i - j) ``, where `` abs `` is the absolute value function.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "loveleetcode", c = "e"
<strong>Output:</strong> [3,2,1,0,1,0,0,1,2,2,1,0]
<strong>Explanation:</strong> The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 3.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aaab", c = "b"
<strong>Output:</strong> [3,2,1,0]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>4</sup></code>
*   `` s[i] `` and `` c `` are lowercase English letters.
*   It is guaranteed that `` c `` occurs at least once in `` s ``.