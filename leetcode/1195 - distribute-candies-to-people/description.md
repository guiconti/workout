We distribute some&nbsp;number of `` candies ``, to a row of __`` n =&nbsp;num_people ``__&nbsp;people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give `` n ``&nbsp;candies to the last person.

Then, we go back to the start of the row, giving `` n&nbsp;+ 1 `` candies to the first person, `` n&nbsp;+ 2 `` candies to the second person, and so on until we give `` 2 * n ``&nbsp;candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.&nbsp; The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length `` num_people ``&nbsp;and sum `` candies ``) that represents the final distribution of candies.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> candies = 7, num_people = 4
<strong>Output:</strong> [1,2,3,1]
<strong>Explanation:</strong>
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> candies = 10, num_people = 3
<strong>Output:</strong> [5,2,3]
<strong>Explanation: </strong>
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
</pre>

&nbsp;

__Constraints:__

*   1 &lt;= candies &lt;= 10^9
*   1 &lt;= num\_people &lt;= 1000