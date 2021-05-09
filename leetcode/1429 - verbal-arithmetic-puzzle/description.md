Given an equation, represented by `` words `` on left side and the `` result `` on right side.

You need to check if the equation is solvable&nbsp;under the following rules:

*   Each character is decoded as one digit (0 - 9).
*   Every pair of different characters they must map to different digits.
*   Each `` words[i] `` and `` result ``&nbsp;are decoded as one number __without__ leading zeros.
*   Sum of numbers on left side (`` words ``) will equal to the number on right side (`` result ``).&nbsp;

Return `` True ``&nbsp;if the equation is solvable otherwise&nbsp;return&nbsp;`` False ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["SEND","MORE"], result = "MONEY"
<strong>Output:</strong> true
<strong>Explanation:</strong> Map 'S'-&gt; 9, 'E'-&gt;5, 'N'-&gt;6, 'D'-&gt;7, 'M'-&gt;1, 'O'-&gt;0, 'R'-&gt;8, 'Y'-&gt;'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
<strong>Output:</strong> true
<strong>Explanation:</strong> Map 'S'-&gt; 6, 'I'-&gt;5, 'X'-&gt;0, 'E'-&gt;8, 'V'-&gt;7, 'N'-&gt;2, 'T'-&gt;1, 'W'-&gt;'3', 'Y'-&gt;4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214</pre>

__Example 3:__

<pre>
<strong>Input:</strong> words = ["THIS","IS","TOO"], result = "FUNNY"
<strong>Output:</strong> true
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> words = ["LEET","CODE"], result = "POINT"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= words.length &lt;= 5 ``
*   `` 1 &lt;= words[i].length, result.length &lt;= 7 ``
*   `` words[i], result `` contain only uppercase English letters.
*   The number of different characters used in the expression is at most `` 10 ``.