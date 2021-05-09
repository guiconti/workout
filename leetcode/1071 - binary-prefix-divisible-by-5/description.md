Given an array `` A `` of `` 0 ``s and `` 1 ``s, consider `` N_i ``: the i-th subarray from `` A[0] `` to `` A[i] ``&nbsp;interpreted&nbsp;as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans&nbsp;`` answer ``, where `` answer[i] `` is `` true ``&nbsp;if and only if `` N_i ``&nbsp;is divisible by 5.

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">[0,1,1]</span>
<strong>Output: </strong><span id="example-output-1">[true,false,false]</span>
<strong>Explanation: </strong>
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
</pre>

__Example 2:__

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,1]</span>
<strong>Output: </strong><span id="example-output-2">[false,false,false]</span>
</pre>

__Example 3:__

<pre>
<strong>Input: </strong><span id="example-input-3-1">[0,1,1,1,1,1]</span>
<strong>Output: </strong><span id="example-output-3">[true,false,false,false,true,false]</span>
</pre>

__Example 4:__

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,1,1,0,1]</span>
<strong>Output: </strong><span id="example-output-4">[false,false,false,false,false]</span>
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= A.length &lt;= 30000 ``
2.   `` A[i] `` is `` 0 `` or `` 1 ``