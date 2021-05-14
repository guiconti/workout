Let's say a positive integer is a __super-palindrome__ if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers `` left `` and `` right `` represented as strings, return _the number of __super-palindromes__ integers in the inclusive range_ `` [left, right] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> left = "4", right = "1000"
<strong>Output:</strong> 4
<strong>Explanation</strong>: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> left = "1", right = "2"
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= left.length, right.length &lt;= 18 ``
*   `` left `` and `` right `` consist of only digits.
*   `` left `` and `` right `` cannot have leading zeros.
*   `` left `` and `` right `` represent integers in the range <code>[1, 10<sup>18</sup>]</code>.
*   `` left `` is less than or equal to `` right ``.