Given an integer array `` arr ``. You have to sort the integers in the array&nbsp;in ascending order by the number of __1's__&nbsp;in their binary representation and in case of two or more integers have the same number of __1's__ you have to sort them in ascending order.

Return _the sorted array_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [0,1,2,3,4,5,6,7,8]
<strong>Output:</strong> [0,1,2,4,8,3,5,6,7]
<strong>Explantion:</strong> [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1024,512,256,128,64,32,16,8,4,2,1]
<strong>Output:</strong> [1,2,4,8,16,32,64,128,256,512,1024]
<strong>Explantion:</strong> All integers have 1 bit in the binary representation, you should just sort them in ascending order.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [10000,10000]
<strong>Output:</strong> [10000,10000]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [2,3,5,7,11,13,17,19]
<strong>Output:</strong> [2,3,5,17,7,11,13,19]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [10,100,1000,10000]
<strong>Output:</strong> [10,100,10000,1000]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 500 ``
*   `` 0 &lt;= arr[i] &lt;= 10^4 ``