We are stacking blocks to form a pyramid. Each block has a color which is a one-letter string.

We are allowed to place any color block `` C `` on top of two adjacent blocks of colors `` A `` and `` B ``, if and only if `` ABC `` is an allowed triple.

We start with a bottom row of `` bottom ``, represented as a single string. We also start with a list of allowed triples `` allowed ``. Each allowed triple is represented as a string of length `` 3 ``.

Return `` true `` _if we can build the pyramid all the way to the top, otherwise_ `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> bottom = "BCD", allowed = ["BCG","CDE","GEA","FFF"]
<strong>Output:</strong> true
<strong>Explanation:</strong>
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> bottom = "AABA", allowed = ["AAA","AAB","ABA","ABB","BAC"]
<strong>Output:</strong> false
<strong>Explanation:</strong>
We cannot stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= bottom.length &lt;= 8 ``
*   `` 0 &lt;= allowed.length &lt;= 200 ``
*   `` allowed[i].length == 3 ``
*   The letters in all input strings are from the set `` {'A', 'B', 'C', 'D', 'E', 'F', 'G'} ``.