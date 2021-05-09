You have `` n `` boxes. You are given a binary string `` boxes `` of length `` n ``, where `` boxes[i] `` is `` '0' `` if the <code>i<sup>th</sup></code> box is __empty__, and `` '1' `` if it contains __one__ ball.

In one operation, you can move __one__ ball from a box to an adjacent box. Box `` i `` is adjacent to box `` j `` if `` abs(i - j) == 1 ``. Note that after doing so, there may be more than one ball in some boxes.

Return an array `` answer `` of size `` n ``, where `` answer[i] `` is the __minimum__ number of operations needed to move all the balls to the <code>i<sup>th</sup></code> box.

Each `` answer[i] `` is calculated considering the __initial__ state of the boxes.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> boxes = "110"
<strong>Output:</strong> [1,1,3]
<strong>Explanation:</strong> The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> boxes = "001011"
<strong>Output:</strong> [11,8,5,4,3,4]</pre>

&nbsp;

__Constraints:__

*   `` n == boxes.length ``
*   `` 1 &lt;= n &lt;= 2000 ``
*   `` boxes[i] `` is either `` '0' `` or `` '1' ``.