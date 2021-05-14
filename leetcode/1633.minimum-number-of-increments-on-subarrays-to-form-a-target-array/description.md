Given an array of positive integers `` target `` and an array `` initial `` of same size with all zeros.

Return the minimum number of operations to form a `` target `` array from `` initial ``&nbsp;if you are allowed to do the following operation:

*   Choose __any__ subarray from `` initial ``&nbsp;and increment each value by one.

The answer is guaranteed to fit within the range of a 32-bit signed integer.
&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> target = [1,2,3,2,1]
<strong>Output:</strong> 3
<strong>Explanation: </strong>We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4&nbsp;(inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3&nbsp;(inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> target = [3,1,1,2]
<strong>Output:</strong> 4
<strong>Explanation: </strong>(initial)[0,0,0,0] -&gt; [1,1,1,1] -&gt; [1,1,1,2] -&gt; [2,1,1,2] -&gt; [3,1,1,2] (target).
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> target = [3,1,5,4,2]
<strong>Output:</strong> 7
<strong>Explanation: </strong>(initial)[0,0,0,0,0] -&gt; [1,1,1,1,1] -&gt; [2,1,1,1,1] -&gt; [3,1,1,1,1] 
                                  -&gt; [3,1,2,2,2] -&gt; [3,1,3,3,2] -&gt; [3,1,4,4,2] -&gt; [3,1,5,4,2] (target).
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> target = [1,1,1,1]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= target.length &lt;= 10^5 ``
*   `` 1 &lt;= target[i] &lt;= 10^5 ``