Given two arrays of integers&nbsp;`` nums `` and `` index ``. Your task is to create _target_ array under the following rules:

*   Initially _target_ array is empty.
*   From left to right read nums\[i\] and index\[i\], insert at index `` index[i] ``&nbsp;the value `` nums[i] ``&nbsp;in&nbsp;_target_ array.
*   Repeat the previous step until there are no elements to read in `` nums `` and `` index. ``

Return the _target_ array.

It is guaranteed that the insertion operations will be valid.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [0,1,2,3,4], index = [0,1,2,2,1]
<strong>Output:</strong> [0,4,1,3,2]
<strong>Explanation:</strong>
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,0], index = [0,1,2,3,0]
<strong>Output:</strong> [0,1,2,3,4]
<strong>Explanation:</strong>
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1], index = [0]
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length, index.length &lt;= 100 ``
*   `` nums.length == index.length ``
*   `` 0 &lt;= nums[i] &lt;= 100 ``
*   `` 0 &lt;= index[i] &lt;= i ``