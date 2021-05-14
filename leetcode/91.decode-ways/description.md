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

Given a string `` s `` containing only digits, return _the __number__ of ways to __decode__ it_.

The answer is guaranteed to fit in a __32-bit__ integer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "12"
<strong>Output:</strong> 2
<strong>Explanation:</strong> "12" could be decoded as "AB" (1 2) or "L" (12).
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "226"
<strong>Output:</strong> 3
<strong>Explanation:</strong> "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "0"
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -&gt; "10" and 'T' -&gt; "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "06"
<strong>Output:</strong> 0
<strong>Explanation:</strong> "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 100 ``
*   `` s `` contains only digits and may contain leading zero(s).