Given an array `` arr ``&nbsp;that represents a permutation of numbers from `` 1 ``&nbsp;to `` n ``. You have a binary string of size&nbsp;`` n ``&nbsp;that initially has all its bits set to zero.

At each step `` i ``&nbsp;(assuming both the binary string and `` arr `` are 1-indexed) from `` 1 `` to&nbsp;`` n ``, the bit at position&nbsp;`` arr[i] ``&nbsp;is set to&nbsp;`` 1 ``. You are given an integer&nbsp;`` m ``&nbsp;and you need to find the latest step at which there exists a group of ones of length&nbsp;`` m ``. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.

Return _the latest step at which there exists a group of ones of length __exactly___&nbsp;`` m ``. _If no such group exists, return_&nbsp;`` -1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [3,5,1,2,4], m = 1
<strong>Output:</strong> 4
<strong>Explanation:
</strong>Step 1: "00<u>1</u>00", groups: ["1"]
Step 2: "0010<u>1</u>", groups: ["1", "1"]
Step 3: "<u>1</u>0101", groups: ["1", "1", "1"]
Step 4: "1<u>1</u>101", groups: ["111", "1"]
Step 5: "111<u>1</u>1", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [3,1,5,4,2], m = 2
<strong>Output:</strong> -1
<strong>Explanation:
</strong>Step 1: "00<u>1</u>00", groups: ["1"]
Step 2: "<u>1</u>0100", groups: ["1", "1"]
Step 3: "1010<u>1</u>", groups: ["1", "1", "1"]
Step 4: "101<u>1</u>1", groups: ["1", "111"]
Step 5: "1<u>1</u>111", groups: ["11111"]
No group of size 2 exists during any step.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1], m = 1
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [2,1], m = 2
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` n == arr.length ``
*   `` 1 &lt;= n &lt;= 10^5 ``
*   `` 1 &lt;= arr[i] &lt;= n ``
*   All integers in&nbsp;`` arr ``&nbsp;are&nbsp;__distinct__.
*   `` 1 &lt;= m&nbsp;&lt;= arr.length ``