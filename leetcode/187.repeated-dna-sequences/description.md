The __DNA sequence__ is composed of a series of nucleotides abbreviated as `` 'A' ``, `` 'C' ``, `` 'G' ``, and `` 'T' ``.

*   For example, `` "ACGAATTCCG" `` is a __DNA sequence__.

When studying __DNA__, it is useful to identify repeated sequences within the DNA.

Given a string `` s `` that represents a __DNA sequence__, return all the __`` 10 ``-letter-long__ sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in __any order__.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
<strong>Output:</strong> ["AAAAACCCCC","CCCCCAAAAA"]
</pre>

__Example 2:__

<pre><strong>Input:</strong> s = "AAAAAAAAAAAAA"
<strong>Output:</strong> ["AAAAAAAAAA"]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s[i] `` is either `` 'A' ``, `` 'C' ``, `` 'G' ``, or `` 'T' ``.