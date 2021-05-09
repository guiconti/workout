Given a string `` s ``. You should re-order the string using the following algorithm:

1.   Pick the __smallest__ character from `` s `` and __append__ it to the result.
2.   Pick the __smallest__ character from `` s `` which is greater than the last appended character to the result and __append__ it.
3.   Repeat step 2 until you cannot pick more characters.
4.   Pick the __largest__&nbsp;character from `` s `` and __append__ it to the result.
5.   Pick the __largest__&nbsp;character from `` s `` which is smaller than the last appended character to the result and __append__ it.
6.   Repeat step 5 until you cannot pick more characters.
7.   Repeat the steps from 1 to 6 until you pick all characters from `` s ``.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return _the result string_ after sorting `` s ``&nbsp;with this algorithm.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "aaaabbbbcccc"
<strong>Output:</strong> "abccbaabccba"
<strong>Explanation:</strong> After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "rat"
<strong>Output:</strong> "art"
<strong>Explanation:</strong> The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> "cdelotee"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "ggggggg"
<strong>Output:</strong> "ggggggg"
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "spo"
<strong>Output:</strong> "ops"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 500 ``
*   `` s `` contains only lower-case English letters.