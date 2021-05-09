A gene string can be represented by an 8-character long string, with choices from `` 'A' ``, `` 'C' ``, `` 'G' ``, and `` 'T' ``.

Suppose we need to investigate a mutation from a gene string `` start `` to a gene string `` end `` where one mutation is defined as one single character changed in the gene string.

*   For example, `` "AACCGGTT" --&gt; "AACCGGTA" `` is one mutation.

There is also a gene bank `` bank `` that records all the valid gene mutations. A gene must be in `` bank `` to make it a valid gene string.

Given the two gene strings `` start `` and `` end `` and the gene bank `` bank ``, return _the minimum number of mutations needed to mutate from _`` start ``_ to _`` end ``. If there is no such a mutation, return `` -1 ``.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
<strong>Output:</strong> 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   `` start.length == 8 ``
*   `` end.length == 8 ``
*   `` 0 &lt;= bank.length &lt;= 10 ``
*   `` bank[i].length == 8 ``
*   `` start ``, `` end ``, and `` bank[i] `` consist of only the characters `` ['A', 'C', 'G', 'T'] ``.