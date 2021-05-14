Given an integer `` n ``, you must transform it into `` 0 `` using the following operations any number of times:

*   Change the rightmost (<code>0<sup>th</sup></code>) bit in the binary representation of `` n ``.
*   Change the <code>i<sup>th</sup></code> bit in the binary representation of `` n `` if the <code>(i-1)<sup>th</sup></code> bit is set to `` 1 `` and the <code>(i-2)<sup>th</sup></code> through <code>0<sup>th</sup></code> bits are set to `` 0 ``.

Return _the minimum number of operations to transform _`` n ``_ into _`` 0 ``_._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> The binary representation of 3 is "11".
"<u>1</u>1" -&gt; "<u>0</u>1" with the 2nd operation since the 0th bit is 1.
"0<u>1</u>" -&gt; "0<u>0</u>" with the 1st operation.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 4
<strong>Explanation:</strong> The binary representation of 6 is "110".
"<u>1</u>10" -&gt; "<u>0</u>10" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"01<u>0</u>" -&gt; "01<u>1</u>" with the 1st operation.
"0<u>1</u>1" -&gt; "0<u>0</u>1" with the 2nd operation since the 0th bit is 1.
"00<u>1</u>" -&gt; "00<u>0</u>" with the 1st operation.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 9
<strong>Output:</strong> 14
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 333
<strong>Output:</strong> 393
</pre>

&nbsp;

__Constraints:__

*   <code>0 &lt;= n &lt;= 10<sup>9</sup></code>