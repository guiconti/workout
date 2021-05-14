Given an array of&nbsp;integers `` arr ``.

We want to select three indices `` i ``, `` j `` and `` k `` where `` (0 &lt;= i &lt; j &lt;= k &lt; arr.length) ``.

Let's define `` a `` and `` b `` as follows:

*   `` a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] ``
*   `` b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k] ``

Note that __^__ denotes the __bitwise-xor__ operation.

Return _the number of triplets_ (`` i ``, `` j `` and `` k ``) Where `` a == b ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [2,3,1,6,7]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,1,1,1,1]
<strong>Output:</strong> 10
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [2,3]
<strong>Output:</strong> 0
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [1,3,5,7,9]
<strong>Output:</strong> 3
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [7,11,12,9,5,2,7,17,22]
<strong>Output:</strong> 8
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 300 ``
*   `` 1 &lt;= arr[i] &lt;= 10^8 ``