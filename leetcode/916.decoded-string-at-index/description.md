An encoded string `` S `` is given.&nbsp; To find and write the _decoded_ string to a tape, the encoded string is read __one character at a time__&nbsp;and the following steps are taken:

*   If the character read is a letter, that letter is written onto the tape.
*   If the character read is a digit (say `` d ``), the entire current tape is repeatedly written&nbsp;`` d-1 ``&nbsp;more times in total.

Now for some encoded string `` S ``, and an index `` K ``, find and return the `` K ``-th letter (1 indexed) in the decoded string.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>S = <span id="example-input-1-1">"leet2code3"</span>, K = <span id="example-input-1-2">10</span>
<strong>Output: </strong><span id="example-output-1">"o"</span>
<strong>Explanation: </strong>
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>S = <span id="example-input-2-1">"ha22"</span>, K = <span id="example-input-2-2">5</span>
<strong>Output: </strong><span id="example-output-2">"h"</span>
<strong>Explanation: </strong>
The decoded string is "hahahaha".  The 5th letter is "h".
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong>S = <span id="example-input-3-1">"a2345678999999999999999"</span>, K = <span id="example-input-3-2">1</span>
<strong>Output: </strong><span id="example-output-3">"a"</span>
<strong>Explanation: </strong>
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
</pre>
</div>
</div>
</div>

&nbsp;

__Constraints:__

*   `` 2 &lt;= S.length &lt;= 100 ``
*   `` S ``&nbsp;will only contain lowercase letters and digits `` 2 `` through `` 9 ``.
*   `` S ``&nbsp;starts with a letter.
*   `` 1 &lt;= K &lt;= 10^9 ``
*   It's guaranteed that `` K ``&nbsp;is less than or equal to the length of the decoded string.
*   The decoded string is guaranteed to have less than `` 2^63 `` letters.