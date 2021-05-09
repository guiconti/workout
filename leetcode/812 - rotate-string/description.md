We are given two strings, `` A `` and `` B ``.

A _shift on `` A ``_ consists of taking string `` A `` and moving the leftmost character to the rightmost position. For example, if `` A = 'abcde' ``, then it will be `` 'bcdea' `` after one shift on `` A ``. Return `` True `` if and only if `` A `` can become `` B `` after some number of shifts on `` A ``.

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> A = 'abcde', B = 'cdeab'
<strong>Output:</strong> true

<strong>Example 2:</strong>
<strong>Input:</strong> A = 'abcde', B = 'abced'
<strong>Output:</strong> false
</pre>

__Note:__

*   `` A `` and `` B `` will have length at most `` 100 ``.