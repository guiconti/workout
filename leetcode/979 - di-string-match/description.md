A permutation `` perm `` of `` n + 1 `` integers of all the integers in the range `` [0, n] `` can be represented as a string `` s `` of length `` n `` where:

*   `` s[i] == 'I' `` if `` perm[i] &lt; perm[i + 1] ``, and
*   `` s[i] == 'D' `` if `` perm[i] &gt; perm[i + 1] ``.

Given a string `` s ``, reconstruct the permutation `` perm `` and return it. If there are multiple valid permutations perm, return __any of them__.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s = "IDID"
<strong>Output:</strong> [0,4,1,3,2]
</pre>

__Example 2:__

<pre><strong>Input:</strong> s = "III"
<strong>Output:</strong> [0,1,2,3]
</pre>

__Example 3:__

<pre><strong>Input:</strong> s = "DDI"
<strong>Output:</strong> [3,2,0,1]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s[i] `` is either `` 'I' `` or `` 'D' ``.