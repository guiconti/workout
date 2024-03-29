Given an array `` arr `` that is a permutation of `` [0, 1, ..., arr.length - 1] ``, we split the array into some number of "chunks" (partitions), and individually sort each chunk.&nbsp; After concatenating them,&nbsp;the result equals the sorted array.

What is the most number of chunks we could have made?

__Example 1:__

<pre>
<strong>Input:</strong> arr = [4,3,2,1,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,0,2,3,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
</pre>

__Note:__

*   `` arr `` will have length in range `` [1, 10] ``.
*   `` arr[i] `` will be a permutation of `` [0, 1, ..., arr.length - 1] ``.

&nbsp;