In a group of N people (labelled `` 0, 1, 2, ..., N-1 ``), each person has different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label `` x ``, simply "person `` x ``".

We'll say that `` richer[i] = [x, y] `` if person `` x ``&nbsp;definitely has more money than person&nbsp;`` y ``.&nbsp; Note that `` richer ``&nbsp;may only be a subset of valid observations.

Also, we'll say `` quiet[x] = q `` if person 

<font face="monospace">x</font>

&nbsp;has quietness `` q ``.

Now, return `` answer ``, where `` answer[x] = y `` if `` y `` is the least quiet person (that is, the person `` y `` with the smallest value of `` quiet[y] ``), among all people&nbsp;who definitely have&nbsp;equal to or more money than person `` x ``.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>richer = <span id="example-input-1-1">[[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]</span>, quiet = <span id="example-input-1-2">[3,2,5,4,6,1,7,0]</span>
<strong>Output: </strong><span id="example-output-1">[5,5,2,5,4,5,6,7]</span>
<strong>Explanation: </strong>
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn't clear if they have more money than person 0.

answer[7] = 7.
Among all people that definitely have equal to or more money than person 7
(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
is person 7.

The other answers can be filled out with similar reasoning.
</pre>
</div>

__Note:__

1.   `` 1 &lt;= quiet.length = N &lt;= 500 ``
2.   `` 0 &lt;= quiet[i] &lt; N ``, all `` quiet[i] `` are different.
3.   `` 0 &lt;= richer.length &lt;= N * (N-1) / 2 ``
4.   `` 0 &lt;= richer[i][j] &lt; N ``
5.   `` richer[i][0] != richer[i][1] ``
6.   `` richer[i] ``'s are all different.
7.   The&nbsp;observations in `` richer `` are all logically consistent.