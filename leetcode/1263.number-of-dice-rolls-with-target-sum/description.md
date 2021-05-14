You have `` d `` dice and each die has `` f `` faces numbered `` 1, 2, ..., f ``.

Return the number of possible ways (out of <code>f<sup>d</sup></code> total ways) __modulo__ 10<sup>9</sup> + 7 to roll the dice so the sum of the face-up numbers equals `` target ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> d = 1, f = 6, target = 3
<strong>Output:</strong> 1
<strong>Explanation: </strong>
You throw one die with 6 faces.  There is only one way to get a sum of 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> d = 2, f = 6, target = 7
<strong>Output:</strong> 6
<strong>Explanation: </strong>
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> d = 2, f = 5, target = 10
<strong>Output:</strong> 1
<strong>Explanation: </strong>
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> d = 1, f = 2, target = 3
<strong>Output:</strong> 0
<strong>Explanation: </strong>
You throw one die with 2 faces.  There is no way to get a sum of 3.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> d = 30, f = 30, target = 500
<strong>Output:</strong> 222616187
<strong>Explanation: </strong>
The answer must be returned modulo 10^9 + 7.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= d, f &lt;= 30 ``
*   `` 1 &lt;= target &lt;= 1000 ``