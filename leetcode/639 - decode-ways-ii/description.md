A message containing letters from `` A-Z `` can be __encoded__ into numbers using the following mapping:

<pre>
'A' -&gt; "1"
'B' -&gt; "2"
...
'Z' -&gt; "26"
</pre>

To __decode__ an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, `` "11106" `` can be mapped into:

*   `` "AAJF" `` with the grouping `` (1 1 10 6) ``
*   `` "KJF" `` with the grouping `` (11 10 6) ``

Note that the grouping `` (1 11 06) `` is invalid because `` "06" `` cannot be mapped into `` 'F' `` since `` "6" `` is different from `` "06" ``.

__In addition__ to the mapping above, an encoded message may contain the `` '*' `` character, which can represent any digit from `` '1' `` to `` '9' `` (`` '0' `` is excluded). For example, the encoded message `` "1*" `` may represent any of the encoded messages `` "11" ``, `` "12" ``, `` "13" ``, `` "14" ``, `` "15" ``, `` "16" ``, `` "17" ``, `` "18" ``, or `` "19" ``. Decoding `` "1*" `` is equivalent to decoding __any__ of the encoded messages it can represent.

Given a string `` s `` containing digits and the `` '*' `` character, return _the __number__ of ways to __decode__ it_.

Since the answer may be very large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "*"
<strong>Output:</strong> 9
<strong>Explanation:</strong> The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
Hence, there are a total of 9 ways to decode "*".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "1*"
<strong>Output:</strong> 18
<strong>Explanation:</strong> The encoded message can represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19".
Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K").
Hence, there are a total of 9 * 2 = 18 ways to decode "1*".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "2*"
<strong>Output:</strong> 15
<strong>Explanation:</strong> The encoded message can represent any of the encoded messages "21", "22", "23", "24", "25", "26", "27", "28", or "29".
"21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27", "28", and "29" only have 1 way.
Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode "2*".
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s[i] `` is a digit or `` '*' ``.