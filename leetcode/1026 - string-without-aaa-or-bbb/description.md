Given two integers `` a `` and `` b ``, return __any__ string `` s `` such that:

*   `` s `` has length `` a + b `` and contains exactly `` a `` `` 'a' `` letters, and exactly `` b `` `` 'b' `` letters,
*   The substring `` 'aaa' `` does not occur in `` s ``, and
*   The substring `` 'bbb' `` does not occur in `` s ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> a = 1, b = 2
<strong>Output:</strong> "abb"
<strong>Explanation:</strong> "abb", "bab" and "bba" are all correct answers.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> a = 4, b = 1
<strong>Output:</strong> "aabaa"
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= a, b &lt;= 100 ``
*   It is guaranteed such an `` s `` exists for the given `` a `` and `` b ``.