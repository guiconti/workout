There are

<font face="monospace">&nbsp;<code>N</code></font>

 dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push&nbsp;some of the dominoes either to the left or to the right.

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/18/domino.png" style="height: 160px;"/>

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino&nbsp;expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state.&nbsp;`` S[i] = 'L' ``, if the i-th domino has been pushed to the left; `` S[i] = 'R' ``, if the i-th domino has been pushed to the right; `` S[i] = '.' ``,&nbsp;if the `` i ``-th domino has not been pushed.

Return a string representing the final state.&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>".L.R...LR..L.."
<strong>Output: </strong>"LL.RR.LLRRLL.."
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>"RR.L"
<strong>Output: </strong>"RR.L"
<strong>Explanation: </strong>The first domino expends no additional force on the second domino.
</pre>

__Note:__

1.   `` 0 &lt;= N&nbsp;&lt;= 10^5 ``
2.   String&nbsp;`` dominoes `` contains only&nbsp;`` 'L ``', `` 'R' `` and `` '.' ``