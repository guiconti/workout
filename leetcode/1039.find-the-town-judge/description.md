In a town, there are `` N `` people labelled from&nbsp;`` 1 `` to `` N ``.&nbsp; There is a rumor that one of these people is secretly the town judge.

If the&nbsp;town judge exists, then:

1.   The town judge trusts nobody.
2.   Everybody (except for the town judge) trusts the town judge.
3.   There is exactly one person that satisfies properties 1 and 2.

You are given `` trust ``, an array of pairs `` trust[i] = [a, b] `` representing that the person labelled `` a `` trusts the person labelled `` b ``.

If the town judge exists and can be identified, return the label of the town judge.&nbsp; Otherwise, return `` -1 ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> N = 2, trust = [[1,2]]
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre><strong>Input:</strong> N = 3, trust = [[1,3],[2,3]]
<strong>Output:</strong> 3
</pre>

__Example 3:__

<pre><strong>Input:</strong> N = 3, trust = [[1,3],[2,3],[3,1]]
<strong>Output:</strong> -1
</pre>

__Example 4:__

<pre><strong>Input:</strong> N = 3, trust = [[1,2],[2,3]]
<strong>Output:</strong> -1
</pre>

__Example 5:__

<pre><strong>Input:</strong> N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= N &lt;= 1000 ``
*   `` 0 &lt;= trust.length &lt;= 10^4 ``
*   `` trust[i].length == 2 ``
*   `` trust[i] `` are all different
*   `` trust[i][0] != trust[i][1] ``
*   `` 1 &lt;= trust[i][0], trust[i][1] &lt;= N ``