You have a bomb to defuse, and your time is running out! Your informer will provide you with a __circular__ array `` code ``&nbsp;of length of `` n ``&nbsp;and a key `` k ``.

To decrypt the code, you must replace every number. All the numbers are replaced __simultaneously__.

*   If `` k &gt; 0 ``, replace the <code>i<sup>th</sup></code> number with the sum of the __next__ `` k `` numbers.
*   If `` k &lt; 0 ``, replace the <code>i<sup>th</sup></code> number with the sum of the __previous__ `` k `` numbers.
*   If `` k == 0 ``, replace the <code>i<sup>th</sup></code> number with `` 0 ``.

As `` code `` is circular, the next element of `` code[n-1] `` is `` code[0] ``, and the previous element of `` code[0] `` is `` code[n-1] ``.

Given the __circular__ array `` code `` and an integer key `` k ``, return _the decrypted code to defuse the bomb_!

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> code = [5,7,1,4], k = 3
<strong>Output:</strong> [12,10,16,13]
<strong>Explanation:</strong> Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> code = [1,2,3,4], k = 0
<strong>Output:</strong> [0,0,0,0]
<strong>Explanation:</strong> When k is zero, the numbers are replaced by 0. 
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> code = [2,4,9,3], k = -2
<strong>Output:</strong> [12,5,6,13]
<strong>Explanation:</strong> The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the <strong>previous</strong> numbers.
</pre>

&nbsp;

__Constraints:__

*   `` n == code.length ``
*   `` 1 &lt;= n&nbsp;&lt;= 100 ``
*   `` 1 &lt;= code[i] &lt;= 100 ``
*   `` -(n - 1) &lt;= k &lt;= n - 1 ``