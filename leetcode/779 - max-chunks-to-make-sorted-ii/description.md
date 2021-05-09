_This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, the input array could be up to length `` 2000 ``, and the elements could be up to `` 10**8 ``._

---

Given an array `` arr `` of integers (__not necessarily distinct__), we split the array into some number of "chunks" (partitions), and individually sort each chunk.&nbsp; After concatenating them,&nbsp;the result equals the sorted array.

What is the most number of chunks we could have made?

__Example 1:__

<pre>
<strong>Input:</strong> arr = [5,4,3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [2,1,3,4,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
</pre>

__Note:__

*   `` arr `` will have length in range `` [1, 2000] ``.
*   `` arr[i] `` will be an integer in range `` [0, 10**8] ``.

&nbsp;