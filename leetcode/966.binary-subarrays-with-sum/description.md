In an array `` A `` of `` 0 ``s and `` 1 ``s, how many __non-empty__ subarrays have sum `` S ``?

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,0,1,0,1]</span>, S = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<strong>Explanation: </strong>
The 4 subarrays are bolded below:
[<strong>1,0,1</strong>,0,1]
[<strong>1,0,1,0</strong>,1]
[1,<strong>0,1,0,1</strong>]
[1,0,<strong>1,0,1</strong>]
</pre>

&nbsp;

__Note:__

1.   `` A.length &lt;= 30000 ``
2.   `` 0 &lt;= S &lt;= A.length ``
3.   `` A[i] ``&nbsp;is either `` 0 ``&nbsp;or `` 1 ``.