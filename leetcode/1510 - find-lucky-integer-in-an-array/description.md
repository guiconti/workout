Given an array of integers `` arr ``, a lucky integer is an integer which has a frequency in the array equal to its value.

Return _a lucky integer_&nbsp;in the array. If there are multiple lucky integers return the __largest__ of them. If there is no lucky&nbsp;integer return __-1__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [2,2,3,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The only lucky number in the array is 2 because frequency[2] == 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,2,2,3,3,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 1, 2 and 3 are all lucky numbers, return the largest of them.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [2,2,2,3,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There are no lucky numbers in the array.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [5]
<strong>Output:</strong> -1
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [7,7,7,7,7,7,7]
<strong>Output:</strong> 7
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 500 ``
*   `` 1 &lt;= arr[i] &lt;= 500 ``