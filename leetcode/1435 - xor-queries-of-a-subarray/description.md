Given the array `` arr `` of positive integers and the array `` queries `` where <code>queries[i] = [L<sub>i,&nbsp;</sub>R<sub>i</sub>]</code>,&nbsp;for each query `` i `` compute the __XOR__ of elements from <code>L<sub>i</sub></code> to `` Ri `` (that is, <code>arr[L<sub>i</sub>] <strong>xor</strong> arr[L<sub>i+1</sub>] <strong>xor</strong> ... <strong>xor</strong> arr[R<sub>i</sub>]</code> ). Return an array containing the result for the given `` queries ``.
&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
<strong>Output:</strong> [2,7,14,8] 
<strong>Explanation:</strong> 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
<strong>Output:</strong> [8,0,4,4]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 3 *&nbsp;10^4 ``
*   `` 1 &lt;= arr[i] &lt;= 10^9 ``
*   `` 1 &lt;= queries.length &lt;= 3 * 10^4 ``
*   `` queries[i].length == 2 ``
*   `` 0 &lt;= queries[i][0] &lt;= queries[i][1] &lt; arr.length ``