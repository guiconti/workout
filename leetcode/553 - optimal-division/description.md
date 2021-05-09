You are given an integer array `` nums ``. The adjacent integers in `` nums `` will perform the float division.

*   For example, for `` nums = [2,3,4] ``, we will evaluate the expression `` "2/3/4" ``.

However, you can add any number of parenthesis at any position to change the priority of operations. You want to add these parentheses such the value of the expression after the evaluation is maximum.

Return _the corresponding expression that has the maximum value in string format_.

__Note:__ your expression should not contain redundant parenthesis.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1000,100,10,2]
<strong>Output:</strong> "1000/(100/10/2)"
<strong>Explanation:</strong>
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, since they don't influence the operation priority. So you should return "1000/(100/10/2)".
Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,3,4]
<strong>Output:</strong> "2/(3/4)"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [2]
<strong>Output:</strong> "2"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 10 ``
*   `` 2 &lt;= nums[i] &lt;= 1000 ``
*   There is only one optimal division for the given iput.