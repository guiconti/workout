You are given an array of `` logs ``. Each log is a space-delimited string of words, where the first word is the __identifier__.

There are two types of logs:

*   __Letter-logs__: All words (except the identifier) consist of lowercase English letters.
*   __Digit-logs__: All words (except the identifier) consist of digits.

Reorder these logs so that:

1.   The __letter-logs__ come before all __digit-logs__.
2.   The __letter-logs__ are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3.   The __digit-logs__ maintain their relative ordering.

Return _the final order of the logs_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
<strong>Output:</strong> ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
<strong>Explanation:</strong>
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
<strong>Output:</strong> ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= logs.length &lt;= 100 ``
*   `` 3 &lt;= logs[i].length &lt;= 100 ``
*   All the tokens of `` logs[i] `` are separated by a __single__ space.
*   `` logs[i] `` is guaranteed to have an identifier and at least one word after the identifier.