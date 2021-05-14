A string is called _happy_ if it does&nbsp;not have any of the strings `` 'aaa' ``, `` 'bbb' ``&nbsp;or `` 'ccc' ``&nbsp;as a substring.

Given three integers `` a ``, `` b `` and `` c ``, return __any__ string `` s ``,&nbsp;which satisfies following conditions:

*   `` s `` is _happy&nbsp;_and longest possible.
*   `` s `` contains __at most__ `` a ``&nbsp;occurrences of the letter&nbsp;`` 'a' ``, __at most__ `` b ``&nbsp;occurrences of the letter `` 'b' `` and __at most__ `` c `` occurrences of the letter `` 'c' ``.
*   `` s&nbsp; ``will only contain `` 'a' ``, `` 'b' `` and `` 'c' ``&nbsp;letters.

If there is no such string `` s ``&nbsp;return the empty string `` "" ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> a = 1, b = 1, c = 7
<strong>Output:</strong> "ccaccbcc"
<strong>Explanation:</strong> "ccbccacc" would also be a correct answer.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> a = 2, b = 2, c = 1
<strong>Output:</strong> "aabbc"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> a = 7, b = 1, c = 0
<strong>Output:</strong> "aabaa"
<strong>Explanation:</strong> It's the only correct answer in this case.
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= a, b, c &lt;= 100 ``
*   `` a + b + c &gt; 0 ``