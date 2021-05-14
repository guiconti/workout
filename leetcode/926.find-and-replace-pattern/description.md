You have a list of&nbsp;`` words `` and a `` pattern ``, and you want to know which words in `` words `` matches the pattern.

A word matches the pattern if there exists a permutation of letters `` p `` so that after replacing every letter `` x `` in the pattern with `` p(x) ``, we get the desired word.

(_Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter._)

Return a list of the words in `` words ``&nbsp;that match the given pattern.&nbsp;

You may return the answer in any order.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>words = <span id="example-input-1-1">["abc","deq","mee","aqq","dkd","ccc"]</span>, pattern = <span id="example-input-1-2">"abb"</span>
<strong>Output: </strong><span id="example-output-1">["mee","aqq"]</span>
<strong><span>Explanation: </span></strong>"mee" matches the pattern because there is a permutation {a -&gt; m, b -&gt; e, ...}. 
"ccc" does not match the pattern because {a -&gt; c, b -&gt; c, ...} is not a permutation,
since a and b map to the same letter.</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ul>
<li><code>1 &lt;= words.length &lt;= 50</code></li>
<li><code>1 &lt;= pattern.length = words[i].length&nbsp;&lt;= 20</code></li>
</ul>
</div>