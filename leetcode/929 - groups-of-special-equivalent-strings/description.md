You are given an array `` A `` of strings.

A _move&nbsp;onto `` S ``_ consists of swapping any two even indexed characters of `` S ``, or any two odd indexed characters of `` S ``.

Two strings `` S `` and `` T `` are&nbsp;_special-equivalent_&nbsp;if after any number of _moves onto `` S ``_, `` S == T ``.

For example, `` S = "zzxy" `` and `` T = "xyzz" `` are special-equivalent because we may make the moves `` "zzxy" -&gt; "xzzy" -&gt; "xyzz" ``&nbsp;that swap `` S[0] `` and `` S[2] ``, then `` S[1] `` and `` S[3] ``.

Now, a _group of special-equivalent strings from `` A ``_&nbsp;is a non-empty subset of&nbsp;A such that:

1.   Every pair of strings in the group are special equivalent, and;
2.   The group is the largest size possible (ie., there isn't a string S not in the group such that S is special equivalent to every string in the group)

Return the number of groups of special-equivalent strings from `` A ``.

<div>&nbsp;</div>

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">["abcd","cdab","cbad","xyzz","zzxy","zzyx"]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong>Explanation: </strong>
One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings are all pairwise special equivalent to these.

The other two groups are ["xyzz", "zzxy"] and ["zzyx"].  Note that in particular, "zzxy" is not special equivalent to "zzyx".
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">["abc","acb","bac","bca","cab","cba"]</span>
<strong>Output: </strong><span id="example-output-2">3</span></pre>
<p>&nbsp;</p>
</div>
</div>

<div>
<div>
<div>
<div>
<p><strong>Note:</strong></p>
<ul>
<li><code>1 &lt;= A.length &lt;= 1000</code></li>
<li><code>1 &lt;= A[i].length &lt;= 20</code></li>
<li>All <code>A[i]</code> have the same length.</li>
<li>All <code>A[i]</code> consist of only lowercase letters.</li>
</ul>
</div>
</div>
</div>
</div>