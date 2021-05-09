There are several stones&nbsp;__arranged in a row__, and each stone has an associated&nbsp;value which is an integer given in the array&nbsp;`` stoneValue ``.

In each round of the game, Alice divides the row into __two non-empty rows__ (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and&nbsp;Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only __one stone remaining__. Alice's is initially __zero__.

Return _the maximum score that Alice can obtain_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> stoneValue = [6,2,3,4,5,5]
<strong>Output:</strong> 18
<strong>Explanation:</strong> In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> stoneValue = [7,7,7,7,7,7,7]
<strong>Output:</strong> 28
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> stoneValue = [4]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= stoneValue.length &lt;= 500 ``
*   `` 1 &lt;=&nbsp;stoneValue[i] &lt;= 10^6 ``