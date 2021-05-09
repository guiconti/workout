Given a fixed length&nbsp;array `` arr `` of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array __in place__, do not return anything from your function.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,0,2,3,0,4,5,0]</span>
<strong>Output: </strong>null
<strong>Explanation: </strong>After calling your function, the <strong>input</strong> array is modified to: <span id="example-output-1">[1,0,0,2,3,0,0,4]</span>
</pre>

__Example 2:__

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,3]</span>
<strong>Output: </strong>null
<strong>Explanation: </strong>After calling your function, the <strong>input</strong> array is modified to: <span id="example-output-2">[1,2,3]</span>
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= arr.length &lt;= 10000 ``
2.   `` 0 &lt;= arr[i] &lt;= 9 ``