Given a string `` s ``. An _awesome_ substring is a non-empty substring of `` s `` such that we can make any number of swaps in order to make it palindrome.

Return the length of the maximum length __awesome substring__ of `` s ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "3242415"
<strong>Output:</strong> 5
<strong>Explanation:</strong> "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "12345678"
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "213123"
<strong>Output:</strong> 6
<strong>Explanation:</strong> "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "00"
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 10^5 ``
*   `` s `` consists only of digits.