Three stones are on a number line at positions `` a ``, `` b ``, and `` c ``.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone), and move it to an unoccupied position between those&nbsp;endpoints.&nbsp; Formally, let's say the stones are currently at positions `` x, y, z `` with `` x &lt; y &lt; z ``.&nbsp; You pick up the stone at either position `` x `` or position `` z ``, and move that stone to an integer position `` k ``, with `` x &lt; k &lt; z `` and `` k != y ``.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?&nbsp; Return the answer as an length 2 array: `` answer = [minimum_moves, maximum_moves] ``

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>a = <span id="example-input-1-1">1</span>, b = <span id="example-input-1-2">2</span>, c = <span id="example-input-1-3">5</span>
<strong>Output: </strong><span id="example-output-1">[1,2]</span>
<strong>Explanation: </strong>Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>a = <span id="example-input-2-1">4</span>, b = <span id="example-input-2-2">3</span>, c = <span id="example-input-2-3">2</span>
<strong>Output: </strong><span id="example-output-2">[0,0]</span>
<strong>Explanation: </strong>We cannot make any moves.
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong>a = <span id="example-input-3-1">3</span>, b = <span id="example-input-3-2">5</span>, c = <span id="example-input-3-3">1</span>
<strong>Output: </strong><span id="example-output-3">[1,2]</span>
<strong>Explanation: </strong>Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.
</pre>
<p>&nbsp;</p>
</div>
</div>

__Note:__

1.   `` 1 &lt;= a &lt;= 100 ``
2.   `` 1 &lt;= b &lt;= 100 ``
3.   `` 1 &lt;= c &lt;= 100 ``
4.   `` a != b, b != c, c != a ``

<div>
<p>&nbsp;</p>
<div>
<div>&nbsp;</div>
</div>
</div>