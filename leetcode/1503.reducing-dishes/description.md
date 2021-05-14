A chef&nbsp;has collected data on the `` satisfaction `` level of his&nbsp;`` n `` dishes.&nbsp;Chef can cook any dish in 1 unit of time.

_Like-time coefficient_&nbsp;of a dish is defined as&nbsp;the time taken to cook that dish including previous dishes multiplied by its satisfaction level &nbsp;i.e.&nbsp; `` time[i] ``\*`` satisfaction[i] ``

Return&nbsp;the maximum sum of&nbsp;_Like-time coefficient _that the chef can obtain after dishes preparation.

Dishes can be prepared in __any __order and the chef can discard some dishes to get this maximum value.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> satisfaction = [-1,-8,0,5,-9]
<strong>Output:</strong> 14
<strong>Explanation: </strong>After Removing the second and last dish, the maximum total <em>Like-time coefficient</em> will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared in one unit of time.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> satisfaction = [4,3,2]
<strong>Output:</strong> 20
<strong>Explanation:</strong> Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> satisfaction = [-1,-4,-5]
<strong>Output:</strong> 0
<strong>Explanation:</strong> People don't like the dishes. No dish is prepared.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> satisfaction = [-2,5,-1,0,3,-3]
<strong>Output:</strong> 35
</pre>

&nbsp;

__Constraints:__

*   `` n == satisfaction.length ``
*   `` 1 &lt;= n &lt;= 500 ``
*   `` -10^3 &lt;=&nbsp;satisfaction[i] &lt;= 10^3 ``