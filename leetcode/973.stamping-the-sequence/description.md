You want to form a `` target ``&nbsp;string of __lowercase letters__.

At the beginning, your sequence is `` target.length ``&nbsp;`` '?' `` marks.&nbsp; You also have a `` stamp ``&nbsp;of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.&nbsp; You can make up to `` 10 * target.length `` turns.

For example, if the initial sequence is 

<font face="monospace">"?????"</font>

, and your stamp is `` "abc" ``,&nbsp; then you may make 

<font face="monospace">"abc??", "?abc?", "??abc"&nbsp;</font>

in the first turn.&nbsp; (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of&nbsp;the index of the left-most letter being stamped at each turn.&nbsp; If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is 

<font face="monospace">"ababc"</font>

, and the stamp is `` "abc" ``, then we could return the answer `` [0, 2] ``, corresponding to the moves 

<font face="monospace">"?????" -&gt; "abc??" -&gt; "ababc"</font>

.

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within `` 10 * target.length ``&nbsp;moves.&nbsp; Any answers specifying more than this number of moves&nbsp;will not be accepted.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>stamp = <span id="example-input-1-1">"abc"</span>, target = <span id="example-input-1-2">"ababc"</span>
<strong>Output: </strong><span id="example-output-1">[0,2]</span>
([1,0,2] would also be accepted as an answer, as well as some other answers.)
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>stamp = <span id="example-input-2-1">"</span><span id="example-input-2-2">abca</span><span>"</span>, target = <span id="example-input-2-2">"</span><span>aabcaca"</span>
<strong>Output: </strong><span id="example-output-2">[3,0,1]</span>
</pre>
<div>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
</div>
</div>

1.   `` 1 &lt;= stamp.length &lt;= target.length &lt;= 1000 ``
2.   `` stamp `` and `` target `` only contain lowercase letters.